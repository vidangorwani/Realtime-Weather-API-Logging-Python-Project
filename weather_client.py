"""Talks to the OpenWeatherMap geocoding API."""
import requests

from config import GEOCODE_URL


def get_coordinates(city: str, api_key: str) -> tuple[float, float]:
    params = {"q": city, "limit": 1, "appid": api_key}
    resp = requests.get(GEOCODE_URL, params=params, timeout=10)
    resp.raise_for_status()
    results = resp.json()
    return results[0]["lat"], results[0]["lon"]
