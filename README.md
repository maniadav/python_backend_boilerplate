# Running the Backend with Docker

## Development Mode
To run the backend in development mode with auto-reload:

1. Using Docker Compose:
   ```bash
   docker-compose up dev
   ```
2. Alternatively, using Docker directly:
   ```bash
   docker build -f Dockerfile.dev -t python-backend-movie-api-dev .
   docker run -p 8000:8000 -v $(pwd):/app -e FLASK_ENV=development python-backend-movie-api-dev
   ```
3. The API will be available at `http://localhost:8000`.

## Production Mode
To run the backend in production mode:

1. Using Docker Compose:
   ```bash
   docker-compose up web
   ```
2. Alternatively, using Docker directly:
   ```bash
   docker build -f Dockerfile.prod -t python-backend-movie-api-prod .
   docker run -p 8000:8000 -e FLASK_ENV=production python-backend-movie-api-prod
   ```
3. The API will be available at `http://localhost:8000`.
