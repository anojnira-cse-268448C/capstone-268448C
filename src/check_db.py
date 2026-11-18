import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

with psycopg.connect(
    host="localhost",
    port=5432,
    dbname=os.environ["POSTGRES_DB"],
    user=os.environ["POSTGRES_USER"],
    password=os.environ["POSTGRES_PASSWORD"],
) as conn:
    print(conn.execute("SELECT version()").fetchone()[0])
