# db_connection.py
import os
import psycopg2
import urllib.parse as up

def get_connection():
    # Parse DATABASE_URL from environment
    up.uses_netloc.append("postgres")
    url = os.environ.get("postgresql://dental_clinic_database_management_user:LVGD1i6DqtbBM6M4nF1ieCW51L1qA2MC@dpg-d1huhp6r433s73bg0q7g-a.oregon-postgres.render.com/dental_clinic_database_management")
    return psycopg2.connect(url)
