import pandas as pd
import os

stock = 'LOW'

# Get CSVs for financial statements
dir = os.getcwd()
income_stmt_file = dir + "/src/data/us-income-annual.csv"
balance_stmt_file = dir + "/src/data/us-balance-annual.csv"
cash_flow_stmt_file = dir + "/src/data/us-cashflow-annual.csv"

# ======== 1. First process income statements
income_stmt_all = pd.read_csv(income_stmt_file, sep=";")

# Slice the income statements df for just the stock we are interested in 
stock_income_stmts = income_stmt_all[income_stmt_all.Ticker == stock]

# Create ultimate stock data df
stock_income_data = stock_income_stmts[["Publish Date", "Report Date", "Shares (Basic)", "Revenue", "Net Income"]].copy()

# Divide the nums by share nums to get per share values -- we will do this at the end with everything
stock_income_data[["Sales Per Share", "EPS"]] = stock_income_data[["Revenue", "Net Income"]].div(stock_income_data["Shares (Basic)"], axis=0)

# ======== 2. Next process the balance sheets 
balance_sheets_all = pd.read_csv(balance_stmt_file, sep=";")

stock_balance_sheets = balance_sheets_all[balance_sheets_all.Ticker == stock]

# Get cols from balance sheet we are interested in
stock_balance_sheets = stock_balance_sheets[["Publish Date", "Report Date", "Total Equity"]].copy()

# ======== 3. Next process the cash flow stmts 
cash_flow_stmts = pd.read_csv(cash_flow_stmt_file, sep=";")

stock_cashflow_stmts = cash_flow_stmts[cash_flow_stmts.Ticker == stock]

# Get cols from cash flow statement we are interested in 
stock_cashflow_stmts = stock_cashflow_stmts[["Publish Date", "Report Date", "Net Cash from Operating Activities"]].copy()


