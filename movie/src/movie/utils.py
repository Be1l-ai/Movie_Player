import requests
import os
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv

load_dotenv()
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
url="http://www.omdbapi.com/"

def fetch_movies_by_keyword(keyword):
    try:
        page = random.randint(1, 5)
        response = requests.get(
            f"{url}?apikey={OMDB_API_KEY}&s={keyword}&type=movie&page={page}",
            timeout=3
        )
        if response.status_code == 200:
            data = response.json()
            if data:
                return [movie["Title"] for movie in data.get("Search", [])]
            else:
                print("What an error")
    except Exception:
        print("Theres an error")
    return []

def get_popular_titles(variable_for_search: list):
    popular_titles = []
    
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_to_keyword = {
            executor.submit(fetch_movies_by_keyword, keyword): keyword 
            for keyword in variable_for_search
        }
        
        for future in as_completed(future_to_keyword):
            titles = future.result()
            popular_titles.extend(titles)
    
    random.shuffle(popular_titles)
    return popular_titles[:18]