"""Builds matplotlib and plotly charts from fetched weather records and saves them to results/."""
from pathlib import Path

import matplotlib.pyplot as plt
import plotly.graph_objects as go

from config import RESULTS_DIR


def _output_dir(city: str, start: str, end: str) -> Path:
    folder = RESULTS_DIR / f"{city.lower().replace(' ', '_')}_{start}_to_{end}"
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def plot_matplotlib(records: list[dict], city: str, start: str, end: str, out_dir: Path) -> None:
    dates = [r["date"] for r in records]

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle(f"Weather history for {city.title()} ({start} to {end})")

    axes[0, 0].plot(dates, [r["temp"] for r in records], color="tab:red", marker="o")
    axes[0, 0].set_title("Temperature (\u00b0C)")
    axes[0, 0].tick_params(axis="x", rotation=45)

    axes[0, 1].plot(dates, [r["humidity"] for r in records], color="tab:blue", marker="o")
    axes[0, 1].set_title("Humidity (%)")
    axes[0, 1].tick_params(axis="x", rotation=45)

    axes[1, 0].plot(dates, [r["pressure"] for r in records], color="tab:green", marker="o")
    axes[1, 0].set_title("Pressure (hPa)")
    axes[1, 0].tick_params(axis="x", rotation=45)

    axes[1, 1].plot(dates, [r["wind_speed"] for r in records], color="tab:purple", marker="o")
    axes[1, 1].set_title("Wind speed (m/s)")
    axes[1, 1].tick_params(axis="x", rotation=45)

    fig.tight_layout()
    fig.savefig(out_dir / "matplotlib_overview.png", dpi=150)
    plt.close(fig)


def plot_plotly(records: list[dict], city: str, start: str, end: str, out_dir: Path) -> None:
    dates = [r["date"] for r in records]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=[r["temp"] for r in records],
                              name="Temperature (\u00b0C)", mode="lines+markers"))
    fig.add_trace(go.Scatter(x=dates, y=[r["humidity"] for r in records],
                              name="Humidity (%)", mode="lines+markers", yaxis="y2"))

    fig.update_layout(
        title=f"Temperature & humidity for {city.title()} ({start} to {end})",
        xaxis_title="Date",
        yaxis=dict(title="Temperature (\u00b0C)"),
        yaxis2=dict(title="Humidity (%)", overlaying="y", side="right"),
        legend=dict(orientation="h"),
    )

    try:
        fig.write_image(str(out_dir / "plotly_interactive.png"), width=1000, height=600)
    except Exception as exc:
        print(f"  (skipped PNG export for plotly chart: {exc})")
    fig.write_html(str(out_dir / "plotly_interactive.html"))
