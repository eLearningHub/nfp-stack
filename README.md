# nfp-stack
A web application built with Next.js, FastAPI, PostgreSQL stack

## Instructions

- Create a Python project using Poetry for the backend:
  ```bash
  cd nfp-stack
  poetry new app
  mv app backend
  cd backend
  poetry add fastapi "uvicorn[standard]" gunicorn psycopg2-binary sqlalchemy alembic "databases[postgresql]" python-dotenv
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
- Start a Poetry shell:
  ```bash
  poetry shell
  ``` 
- Initialize `alembic` with: 
  ```bash
  alembic init alembic
  ```
- Define `DATABASE_URL` from `env.txt` as an environment variable:
  ```
  export DATABASE_URL=postgresql://nfp_boilerplate_user:password@ep-fun-trip-566065.us-east-2.aws.neon.tech/neondb
  ```
  Note that you need to change `postgres` to `postgresql`
- Modify `alembic/env.py` by adding one line to set the `sqlalchemy.url` option:
  ```python
  # this is the Alembic Config object, which provides
  # access to the values within the .ini file in use.
  config = context.config
  
  config.set_main_option('sqlalchemy.url', os.environ.get("DATABASE_URL"))
  ```
- Generate the first migration file:
  ```bash
  alembic revision -m "create notes table"
  ```
- To actually run the migration, run the same command without the --sql flag:
  ```bash
  alembic upgrade head
  ```

## References

- [nfp-boilerplate](https://github.com/travisluong/nfp-boilerplate)