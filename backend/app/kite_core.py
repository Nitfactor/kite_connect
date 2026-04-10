from kiteconnect import KiteConnect
import os
from dotenv import load_dotenv
import os.path

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

api_key = os.getenv("KITE_API_KEY")
api_secret = os.getenv("KITE_API_SECRET")


def _get_kite_instance():
	return KiteConnect(api_key=api_key)


def get_login_url():
	kite = _get_kite_instance()
	return kite.login_url()


def create_session(request_token: str):
	kite = _get_kite_instance()
	data = kite.generate_session(request_token, api_secret=api_secret)
	kite.set_access_token(data["access_token"])
	return kite



