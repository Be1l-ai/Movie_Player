from flask import Flask, render_template
import os

app = Flask(__name__)

from movie import movie_bp
app.register_blueprint(movie_bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'MovieForCutie is running!'}, 200

if __name__ == "__main__":
    # For local development
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))