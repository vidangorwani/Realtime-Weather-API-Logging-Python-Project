"""Entry point: prompts the user, fetches historical weather, and saves charts."""
from datetime import datetime, timedelta

from config import get_api_key
from weather_client import fetch_history, WeatherAPIError
from plotting import generate_all_plots


def prompt_inputs():
    city = input("Enter city name: ").strip()
    start_str = input("Enter start date (YYYY-MM-DD): ").strip()
    days_str = input("How many days of history do you want to plot? ").strip()
    start_date = datetime.strptime(start_str, "%Y-%m-%d")
    num_days = int(days_str)
    return city, start_date, num_days


def main():
    api_key = get_api_key()
    city, start_date, num_days = prompt_inputs()
    end_date = start_date + timedelta(days=num_days - 1)

    print(f"\nFetching {num_days} day(s) of weather history for {city}...")
    try:
        records = fetch_history(city, start_date, num_days, api_key)
    except WeatherAPIError as exc:
        print(f"Error: {exc}")
        return

    if not records:
        print("No weather data was retrieved.")
        return

    out_dir = generate_all_plots(
        records, city, start_date.date().isoformat(), end_date.date().isoformat()
    )
    print(f"\nSaved plots to: {out_dir}")


if __name__ == "__main__":
    main()
