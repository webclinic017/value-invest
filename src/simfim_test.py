import pandas as pd
import os

stock = 'LOW'

stock_df = {}

# Open CSV for income statements
dir = os.getcwd()
file = dir + "/src/data/us-income-annual.csv"

df = pd.read_csv(file, sep=";")

# Slice the df for just the stock we are interested in 
stock_data = df[df.Ticker == stock]
shares = stock_data[["Publish Date", "Shares (Basic)"]]

print(shares)
