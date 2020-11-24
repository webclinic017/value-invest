import pandas as pd
import psycopg2
import database as db
import os
import yfinance as yf

CURRENT_FY = 2020

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

    x = 0
    for s in stocks_list:
        x += 1
        if x > 5: break
        print(s)
        # Go through each stock, compare to stocks recognized by (Alpha Vantage, Yahoo Finance)
        stock = yf.Ticker(s)
        print(stock.cashflow)




if __name__ == "__main__":
    update()