def show_margins(kite):
    try:
        margins = kite.margins()
        live_balance = margins["equity"]["available"]["live_balance"]
        print(f"Available cash to use: {live_balance}")
    except Exception as e:
        print(f"Error: {e}")
