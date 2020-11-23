import psycopg2 
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv()

try:
    connection = psycopg2.connect(user = os.environ.get("DB-USER"),
                                    password = os.environ.get("PASSWORD"),
                                    host = os.environ.get("HOST"),
                                    port = os.environ.get("PORT"), 
                                    database = os.environ.get("DATABASE"))

    cursor = connection.cursor()

    # Print PostgreSQL connection props
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")

    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except Exception as e:
    print("Error while connecting to Postgres DB:", e)

finally:
    # Closing db connection
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")