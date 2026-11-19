"""Shared settings for the data pipeline scripts.

Secrets are read from environment variables (or a local `.env` file),
never from the code. Copy `.env.example` to `.env` and fill in your values.
"""
import os
import urllib.parse
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # python-dotenv is optional; plain env vars also work
    pass

FIRMS_MAP_KEY = os.getenv("FIRMS_MAP_KEY", "")

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "5433")
DB_NAME = os.getenv("DB_NAME", "uk_cat_model")

DATA_DIR = Path(os.getenv("DATA_DIR", Path(__file__).parent / "data"))


def database_url() -> str:
    """PostgreSQL connection string built from the environment."""
    password = urllib.parse.quote_plus(DB_PASSWORD)
    return f"postgresql://{DB_USER}:{password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def require_firms_key() -> str:
    if not FIRMS_MAP_KEY:
        raise SystemExit(
            "FIRMS_MAP_KEY is not set. Add it to your .env file "
            "(get a key at https://firms.modaps.eosdis.nasa.gov/api/map_key/)."
        )
    return FIRMS_MAP_KEY
