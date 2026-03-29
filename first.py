# This is Rabola.com 
import yfinance as yf
import pandas as pd

ticker = yf.Ticker("TCS.NS")

df = ticker.history(period="1mo")
print(df[["Open", "Close", "Volume"]])