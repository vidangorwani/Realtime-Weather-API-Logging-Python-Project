"""Shared configuration and API key handling."""
import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results"

GEOCODE_URL = "https://api.openweathermap.org/geo/1.0/direct"
TIMEMACHINE_URL = "https://api.openweathermap.org/data/3.0/onecall/timemachine"


def get_api_key() -> str:
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        api_key = input("Enter your OpenWeatherMap API key: ").strip()
    return api_key
