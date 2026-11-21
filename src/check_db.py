import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def check_db_connection():
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
    ) as conn:
        print(conn.execute("SELECT version()").fetchone()[0])

import pandas as pd
def check_state_counts():
    [print(s, pd.read_csv(f'data/synthea/output/{s}/csv/patients.csv', usecols=['STATE'])['STATE'].value_counts().to_dict()) for s in ['massachusetts','texas','florida']]