from flask import Flask, render_template

app = Flask(__name__)

from movie import movie_bp
app.register_blueprint(movie_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)