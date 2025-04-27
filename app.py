from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load movie data from the JSON file
def load_movies():
    with open('movies.json', 'r') as file:
        return json.load(file)

import time


@app.route('/')
def hello():
    return f'Hello World! I have been summoned!\n'

@app.route('/api/movies', methods=['GET'])
def get_movies():
    """Return the list of all movies."""
    movies = load_movies()
    return jsonify(movies)

@app.route('/api/movies/<int:movie_id>', methods=['GET'])
def get_movie_details(movie_id):
    """Return details of a specific movie by ID."""
    movies = load_movies()
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie:
        return jsonify(movie)
    else:
        return jsonify({"error": "Movie not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
