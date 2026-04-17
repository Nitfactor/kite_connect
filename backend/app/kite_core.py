from kiteconnect import KiteConnect
import os
from dotenv import load_dotenv
from routes.margins import show_margins

load_dotenv()
api_key = os.getenv("KITE_API_KEY")
api_secret = os.getenv("KITE_API_SECRET")
kite = KiteConnect(api_key=api_key)

print("1. Login here to get your request token:", kite.login_url())
request_token = input("2. Enter the request_token from the URL: ") 
data = kite.generate_session(request_token, api_secret=api_secret)
kite.set_access_token(data["access_token"])

show_margins(kite)