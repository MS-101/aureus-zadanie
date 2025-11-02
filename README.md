# Python backend server

This repository contains an implementation of REST API service for management of loans.

## Requirements

-   python 3.13.1
-   PostgreSQL
-   Docker
-   fastapi
-   uvicorn
-   sqlalchemy
-   psycopg2

## Installation Guide

### Virtual enviroment

You will need to install PostgreSQL (https://www.postgresql.org/) on your server and create database using database dump **db/init.sql**

1. Create virtual environment: `python -m venv .venv`
2. Activate virtual environment: `source .venv/bin/activate`
3. Install requirements: `pip install -r requirements.txt`
4. Create .env file according to .env.example
5. Run server: `uvicorn src.main:app --reload --port 80`

Explain here how to set up .venv, install requirements.txt and run server using uvicorn

### Docker

1. Create .env file according to .env.example (DB_HOST and DB_PORT will be set automatically)
1. Install Docker: https://www.docker.com/
1. Build and run the containers using command: `docker compose up --build`

## User Guide

The following endpoints have been implemented:

-   **GET** /contact/info
-   **POST** /contact/info
-   **GET** /loans
-   **GET** /loan

In order to test these endpoints you can use the built in fastapi documentation on route: **/docs**
