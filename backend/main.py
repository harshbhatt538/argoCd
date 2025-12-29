from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

# 1. Get Secrets from Environment Variables (injected by K8s)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "password")
DB_NAME = "appdb"

@app.get("/")
def read_root():
    try:
        # 2. Try to connect to the Database
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        conn.close()
        return {"message": "Hello from FastAPI!", "db_status": "Connected to Postgres Successfully!"}
    except Exception as e:
        return {"message": "Hello from FastAPI!", "db_status": f"Connection Failed: {str(e)}"}
