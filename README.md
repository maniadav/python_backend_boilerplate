# Movie API

A RESTful API for managing movies and actors built with Flask, SQLAlchemy, and Marshmallow.

## Features

- CRUD operations for movies and actors
- Relationship management between movies and actors
- Data validation
- Error handling
- SQLite database (configurable to use other databases)

## API Endpoints

### Movies

- `GET /api/movies` - Get all movies
- `GET /api/movies/<id>` - Get a specific movie
- `POST /api/movies` - Create a new movie
- `PUT /api/movies/<id>` - Update a movie
- `DELETE /api/movies/<id>` - Delete a movie

### Actors

- `GET /api/actors` - Get all actors
- `GET /api/actors/<id>` - Get a specific actor
- `POST /api/actors` - Create a new actor
- `PUT /api/actors/<id>` - Update an actor
- `DELETE /api/actors/<id>` - Delete an actor

### Movie-Actor Relationships

- `GET /api/movies/<movie_id>/actors` - Get all actors for a specific movie
- `POST /api/movies/<movie_id>/actors` - Add an actor to a movie
- `DELETE /api/movies/<movie_id>/actors/<actor_id>` - Remove an actor from a movie

## Setup and Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd python_backend_movie_api
   ```
2. Create a virtual environment and activate it:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
4. Configure environment variables (optional):

   - Edit the `.env` file to customize settings
5. Run the application:

   ```
   python main.py
   ```
6. The API will be available at `http://localhost:5000`

## API Usage Examples

### Create a Movie

```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "title": "Inception",
  "director": "Christopher Nolan",
  "release_year": 2010,
  "genre": "Sci-Fi",
  "rating": 8.8,
  "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."
}' http://localhost:5000/api/movies
```

### Create an Actor

```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "name": "Leonardo DiCaprio",
  "birth_date": "1974-11-11",
  "biography": "Leonardo Wilhelm DiCaprio is an American actor and film producer."
}' http://localhost:5000/api/actors
```

### Add an Actor to a Movie

```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "actor_id": 1
}' http://localhost:5000/api/movies/1/actors
```

## Data Models

### Movie

- `id`: Integer (Primary Key)
- `title`: String (Required)
- `director`: String
- `release_year`: Integer
- `genre`: String
- `rating`: Float
- `description`: Text
- `poster_url`: String
- `created_at`: DateTime
- `updated_at`: DateTime

### Actor

- `id`: Integer (Primary Key)
- `name`: String (Required)
- `birth_date`: Date
- `biography`: Text
- `created_at`: DateTime
- `updated_at`: DateTime

## Running the Backend with Docker

To run the backend code and expose the API for testing using Docker, follow these steps:

1. Build the Docker image:

   ```bash
   docker build -t python-backend-movie-api .
   ```
2. Run the Docker container and expose the API:

   ```bash
   docker run -p 8000:5000 python-backend-movie-api
   ```
3. The API will be available for testing at `http://localhost:8000`.
