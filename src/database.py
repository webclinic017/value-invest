import psycopg2 
import pandas as pd
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv()

def connect_db():
    """
    Connect to the PostgreSQL database 
    Hosted on the Digital Ocean server droplet
    """
    conn = None
    try: 
        # Connect to the PostgreSQL server
        print("Connecting to the Postgres DB...")
        conn = psycopg2.connect(user = os.environ.get("DB-USER"),
                                password = os.environ.get("PASSWORD"),
                                host = os.environ.get("HOST"),
                                port = os.environ.get("PORT"), 
                                database = os.environ.get("DATABASE")
        )
    except (Exception, psycopg2.DatabaseError) as e:
        print(f"Error connecting to DB: {e}")
        sys.exit(1)
    
    print("Database connection successful.")
    return conn


def postgres_to_df(conn, query, column_names):
    """
    Transform result of a SELECT query into a pandas
    dataframe, and return resultant df
    """
    cursor = conn.cursor()

    try:
        cursor.execute(query)
    
    except (Exception, psycopg2.DatabaseError) as e:
        print(f"Error performing query: {e}")
        cursor.close()
        return 1

    # Returns a list of tuples
    tuples = cursor.fetchall()
    cursor.close()

    # Now turn tuples into pandas DF
    df = pd.DataFrame(tuples, columns=column_names)
    return df


if __name__ == "__main__":

    # Test database connection

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