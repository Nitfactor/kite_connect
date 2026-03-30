# This is Rabola.com 
import yfinance as yf
import pandas as pd

ticker = yf.Ticker("TATASTEEL.NS")

df = ticker.history(period="max")
print(df[["Open", "Close", "Volume", ]])

df.to_csv("TATASTEELData.csv")
