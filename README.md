# nfp-stack
A web application built with Next.js, FastAPI, PostgreSQL stack

## Instructions

- Create a Python project using Poetry for the backend:
  ```bash
  cd nfp-stack
  poetry new app
  mv app backend
  cd backend
  poetry add fastapi "uvicorn[standard]" gunicorn psycopg2 sqlalchemy alembic "databases[postgresql]" python-dotenv
  ```
- Create a Postgresql database on [neon.tech](https://neon.tech/) and download the `env.txt` file.
- Install `psql`, a cli tool for communicating with Postgres databases with:
  ```bash
  sudo apt-get install -y postgresql-client
  ```
- You can now connect to your database with:
  ```bash
  psql -h pg.neon.tech
  ```
