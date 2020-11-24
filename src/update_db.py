import pandas as pd
import psycopg2
import database as db
import os

CURRENT_FY = 2020
API-KEY = os.environ.get("AV-API-TOKEN")

def update():

    # Connect to postgres db
    conn = db.connect_db()

    # Connect to db and return list of stocks
    stocks_query = f"""SELECT DISTINCT
                            ticker
                        FROM 
                            d_securities"""
    stocks_cols = ["Stocks"]
    stocks_list = db.postgres_to_df(conn, stocks_query, stocks_cols)["Stocks"]

    cleaned_stocks = []
    for s in stocks_list:
        # Go through each stock, compare to stocks recognized by (Alpha Vantage, Yahoo Finance)
        cleaned_stocks.append(s)

    print(len(cleaned_stocks))

if __name__ == "__main__":
    update()