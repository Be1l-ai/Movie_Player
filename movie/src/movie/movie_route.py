from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")
url = "http://www.omdbapi.com/"

from . import movie_bp

@movie_bp.route("/movies")
def movies():
    search_query = request.args.get("search", "")

    if search_query:
        # Search movies on OMDb
        response = requests.get(url,
            params={
                "apikey": OMDB_API_KEY,
                "s": search_query,
                "type": "movie"
            }
        )
        data = response.json()
        movies_data = data.get("Search", [])
    else:
        popular_titles = [
            "The Shawshank Redemption",
            "The Dark Knight",
            "Inception",
            "Interstellar",
            "The Matrix",
            "Forrest Gump",
            "Pulp Fiction",
            "The Lord of the Rings",
            "Spirited Away",
            "Your Name"
        ]
        
        movies_data = []
        for title in popular_titles:
            response = requests.get(url,
                params={
                    "apikey": OMDB_API_KEY,
                    "t": title,
                    "type": "movie"
                }
            )
            movie = response.json()
            if movie.get("Response") == "True":
                # Format to match Search response structure
                movies_data.append({
                    "Title": movie.get("Title"),
                    "Year": movie.get("Year"),
                    "imdbID": movie.get("imdbID"),
                    "Poster": movie.get("Poster")
                })

    return render_template("movie.html", movies=movies_data, search_query=search_query)

@movie_bp.route("/movie/<imdb_id>")
def movie_detail(imdb_id):
    # Get movie details from OMDb using IMDB ID
    response = requests.get(url,
        params={
            "apikey": OMDB_API_KEY,
            "i": imdb_id,
            "plot": "full"
        }
    )
    movie = response.json()

    stream_url = f"https://vidsrc.to/embed/movie/{imdb_id}"

    return render_template("movie_details.html", movie=movie, stream_url=stream_url)

if __name__ == "__main__":
    pass