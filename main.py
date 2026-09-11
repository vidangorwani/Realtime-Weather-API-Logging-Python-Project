"""Entry point: prompts the user for the query parameters."""
from datetime import datetime


def prompt_inputs():
    city = input("Enter city name: ").strip()
    start_str = input("Enter start date (YYYY-MM-DD): ").strip()
    days_str = input("How many days of history do you want to plot? ").strip()
    start_date = datetime.strptime(start_str, "%Y-%m-%d")
    num_days = int(days_str)
    return city, start_date, num_days


if __name__ == "__main__":
    prompt_inputs()
