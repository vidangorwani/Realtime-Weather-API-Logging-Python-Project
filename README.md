# Weather App

Fetches historical weather data for a city from OpenWeatherMap and plots
temperature, humidity, pressure, and wind speed with matplotlib and plotly.
Charts are saved as images under `results/<city>_<start>_to_<end>/`.

## Setup

```
pip install -r requirements.txt
cp .env.example .env   # then fill in OPENWEATHER_API_KEY
```

You need an OpenWeatherMap API key with access to the "One Call API 3.0"
(the timemachine endpoint used for historical data).

## Run

```
python main.py
```

You'll be prompted for:
- City name
- Start date (`YYYY-MM-DD`)
- Number of days of history to plot

## Files

- `config.py` \u2014 API key loading and shared constants
- `weather_client.py` \u2014 geocoding + historical weather API calls
- `plotting.py` \u2014 matplotlib/plotly chart generation
- `main.py` \u2014 CLI entry point
