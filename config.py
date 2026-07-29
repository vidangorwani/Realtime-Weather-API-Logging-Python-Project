"""Shared configuration and API key handling."""
import os

GEOCODE_URL = "https://api.openweathermap.org/geo/1.0/direct"
TIMEMACHINE_URL = "https://api.openweathermap.org/data/3.0/onecall/timemachine"


def get_api_key() -> str:
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        api_key = input("Enter your OpenWeatherMap API key: ").strip()
    return api_key
