from kiteconnect import KiteConnect

api_key = "3ekhrcyjy3d7o7t1"
api_secret = "7cwwrmcb0prx3t46qy8zlspemin6798u"
kite = KiteConnect(api_key=api_key)

print("1. Login here to get your request token:", kite.login_url())
request_token = input("2. Enter the request_token from the URL: ")
data = kite.generate_session(request_token, api_secret=api_secret)
kite.set_access_token(data["access_token"])

holdings = kite.holdings()

for stock in holdings:
    print(f"Stock: {stock['tradingsymbol']}")
    print(f"  Quantity: {stock['quantity']}")
    print(f"  Average Price: {stock['average_price']}")
    print(f"  P&L: {stock['pnl']}")
    print("-" * 20)

margins = kite.margins()

available_cash = margins["equity"]["available"]["cash"]
live_balance = margins["equity"]["available"]["live_balance"]

print(f"Cash: {available_cash}")
print(f"Usable Right Now: ₹{live_balance}")

