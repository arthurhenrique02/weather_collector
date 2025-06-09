from fastapi import FastAPI
from .config import configure_cors, configure_routes, configure_db
from dotenv import load_dotenv
import os

load_dotenv()

def start_app() -> FastAPI:
    app = FastAPI(
        debug=os.getenv("DEBUG", "false").lower() == "true",
        title="Weather API",
        version="1.0.0"
    )
    configure_cors(app)
    configure_routes(app)
    configure_db()
    return app


app = start_app()