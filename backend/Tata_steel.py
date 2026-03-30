import os
import yfinance as yf
import pandas as df

symbol = "TATASTEEL.NS"
ticker = yf.Ticker(symbol)
folder = symbol.replace(".", "_")
os.makedirs(folder, exist_ok=True)
print(symbol)

datasets = {
    "history":                  ticker.history(period="1d"),
    "financials":               ticker.financials,
    "balance_sheet":            ticker.balance_sheet,
}

for name, df in datasets.items():
    if df is not None and not df.empty:
        df.to_csv(f"Steel.csv")
        print(f"Saved as Steel.csv")
    else:
        print(f"✗ Skipped {name} — no data")