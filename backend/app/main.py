from fastapi import FastAPI, HTTPException, Query
from typing import Optional
import os
from dotenv import load_dotenv
import os.path

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

from . import kite_core
from . import margins

app = FastAPI()

@app.get("/login")
def login():
    try:
        url = kite_core.get_login_url()
        return {"login_url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/margins")
def get_margins(request_token: Optional[str] = Query(None, description="Request token from Zerodha redirect")):
    if not request_token:
        raise HTTPException(status_code=400, detail="request_token query parameter is required")

    try:
        kite = kite_core.create_session(request_token)
        margins.show_margins(kite)
        return {"status": "margins fetched - check server logs for printed output"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# AI generated 
