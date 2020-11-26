import pandas as pd
import psycopg2
import database as db
import os
import yfinance as yf

CURRENT_FY = 2020
# These are the options available to update db
TO_UPDATE_LIST = ["industries", "stocks"]
# This is the selection chosen to update
UPDATE = "none"

def update_industries(conn):

    # Open CSV file containing data to be used for update
    dir = os.getcwd()
    update_file = dir + "/src/data/companylist.csv"

    new_data = pd.read_csv(update_file, sep=",")
    new_data['Symbol'] = new_data['Symbol'].str.replace('^','-')
    print(new_data.head(n=10))

    # Get unique sector and industries
    unique_entries = new_data.groupby(["Sector", "industry"]).size().reset_index().rename(columns={0:'count'})
    #print(unique_entries)

    # Create DB cursor
    cur = conn.cursor()

    # Loop through unique entries and query DB to check for existence
    for index, row in unique_entries.iterrows():
        sector = row["Sector"]
        industry = row["industry"]
        query = (f"""SELECT EXISTS(SELECT * FROM d_industries d
                    WHERE d.sector = '{sector}'
                    AND d.industry = '{industry}');
                    """)
        cur.execute(query)
        #print(cur.fetchone()[0])


def update_stocks_table(conn):
    '''
    This function takes a CSV of stock symbols named "companylist.csv"
    Must container columns Symbol, Name, Sector, Industry
    Writes them to the database
    '''

    # Open CSV file containing stock list
    dir = os.getcwd()
    update_file = dir + "/src/data/companylist.csv"

    new_data = pd.read_csv(update_file, sep=",")
    new_data['Symbol'] = new_data['Symbol'].str.replace('^','-')
    new_data['Name'] = new_data['Name'].str.replace('&#39;',"'")

    # Get the columns we are interested in and save to temp csv
    new_data = new_data[["Symbol", "Name", "Sector", "industry"]].copy()
    new_data = new_data.rename(columns={
                "Symbol":"ticker",
                "Name":"company_name",
                "Sector":"sector",
                "industry":"industry"})

    # Create a list of tuples from the DF
    tuples = [tuple(x) for x in new_data.to_numpy()]

    # Comma-separated df column names
    cols = ','.join(list(new_data.columns))
    table_name = 'd_stocks'

    # Craft the query
    query = f"""INSERT INTO {table_name} ({cols}) VALUES (%s,%s,%s,%s)"""

    # Create DB cursor
    cursor = conn.cursor()
    
    try:
        cursor.executemany(query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        print(f"Error: {e}")
        conn.rollback()
        cursor.close()
        return 1
    print(f"Stocks added to table complete.")
    cursor.close()
  

def update():

    # Connect to postgres db
    conn = db.connect_db()

    # Section to deal with industry update routing
    if UPDATE == "industries":
        update_industries(conn)

    if UPDATE == "stocks":
        update_stocks_table(conn)

    '''
    stocks_query = f"""SELECT DISTINCT
                            ticker
                        FROM 
                            d_securities"""
    stocks_cols = ["Stocks"]
    stocks_list = db.postgres_to_df(conn, stocks_query, stocks_cols)["Stocks"]
    '''



if __name__ == "__main__":
    update()