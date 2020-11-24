import database as db
import pandas as pd

def start():
    '''
    This is the main function of the project
    Connects to Postgres DB
    Retrieves stock fundamental data and runs value cals
    '''
    STOCK = 'TSLA'

    # Connect to postgres db
    conn = db.connect_db()

    # Get income statement relevant columns for stock of interest
    income_stmt_query = f"""SELECT
                                ticker, 
                                report_date, 
                                shares_basic, 
                                revenue, 
                                net_income
                            FROM 
                                f_income_stmts_annual
                            WHERE 
                                ticker = '{STOCK}';"""

    income_df_columns = ["Ticker", "Date", "Shares", "Revenue", "Net Income"]

    income_df = db.postgres_to_df(conn, income_stmt_query, income_df_columns)

    # Get balance sheet columns
    balance_stmt_query = f"""SELECT
                                total_equity
                            FROM 
                                f_balance_sheets_annual b
                            WHERE 
                                b.ticker = '{STOCK}';"""
    balance_df_cols = ["Total Equity"]
    balance_df = db.postgres_to_df(conn, balance_stmt_query, balance_df_cols)

    # Get cash flow stmt columns
    cashflow_stmt_query = f"""SELECT
                                net_cash_operating_activities
                            FROM 
                                f_cashflow_annual c
                            WHERE 
                                c.ticker = '{STOCK}';"""
    cashflow_df_cols = ["Net Cash from Operating Act."]
    cashflow_df = db.postgres_to_df(conn, cashflow_stmt_query, cashflow_df_cols)

    # Join 3 resultant dfs together 
    stock_df = pd.concat([income_df, balance_df, cashflow_df], axis=1, sort=False)
    print(stock_df)



if __name__ == "__main__":
    start()