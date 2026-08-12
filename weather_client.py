"""Talks to the OpenWeatherMap geocoding and historical (timemachine) APIs."""
from datetime import datetime, timezone

import requests

from config import GEOCODE_URL, TIMEMACHINE_URL


class WeatherAPIError(RuntimeError):
    pass


def get_coordinates(city: str, api_key: str) -> tuple[float, float]:
    params = {"q": city, "limit": 1, "appid": api_key}
    resp = requests.get(GEOCODE_URL, params=params, timeout=10)
    resp.raise_for_status()
    results = resp.json()
    if not results:
        raise WeatherAPIError(f"Could not find a location matching '{city}'")
    return results[0]["lat"], results[0]["lon"]


def get_historical_weather(lat: float, lon: float, day: datetime, api_key: str) -> dict:
    dt = int(day.replace(hour=12, minute=0, second=0, tzinfo=timezone.utc).timestamp())
    params = {"lat": lat, "lon": lon, "dt": dt, "appid": api_key, "units": "metric"}
    resp = requests.get(TIMEMACHINE_URL, params=params, timeout=10)
    resp.raise_for_status()
    payload = resp.json()
    entries = payload.get("data") or [payload.get("current")]
    entry = entries[0]
    return {
        "date": day.date().isoformat(),
        "temp": entry.get("temp"),
        "feels_like": entry.get("feels_like"),
        "humidity": entry.get("humidity"),
        "pressure": entry.get("pressure"),
        "wind_speed": entry.get("wind_speed"),
        "clouds": entry.get("clouds"),
    }
