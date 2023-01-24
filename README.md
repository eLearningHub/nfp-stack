# nfp-stack
A web application built with Next.js, FastAPI, PostgreSQL stack

## Instructions

```bash
cd nfp-stack
poetry new app
mv app backend
cd backend
poetry add fastapi "uvicorn[standard]" gunicorn psycopg2 sqlalchemy alembic "databases[postgresql]" python-dotenv
```