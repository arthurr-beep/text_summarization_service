## A Sample FASTAPI projects - to demonstrate basic REST OPERATIONS

This is just a basic REST API using FastAPI

## Technologies and Dependencies

1. FastAPI
2. Tortoise ORM and PostgreSQL
3. Docker and docker-compose
4. Pytest for integration Tests
5. Newspaper3k for text summarization (alternatively I could write a scraper and summarize using bart)
6. BackgroundTask to handle post summarization to avoid blocking the post api call


## To Run

make sure docker and docker-compose are installed 
From root directory run the below command

> docker-compose up -d --build

Navigate to localhost:8004/docs to see the api

from command line to run tests - 
> docker-compose exec api python -m pytest ./tests --cov="."
