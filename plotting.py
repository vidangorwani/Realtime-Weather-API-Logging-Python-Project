"""Builds matplotlib charts from fetched weather records and saves them to results/."""
from pathlib import Path

import matplotlib.pyplot as plt

from config import RESULTS_DIR


def _output_dir(city: str, start: str, end: str) -> Path:
    folder = RESULTS_DIR / f"{city.lower().replace(' ', '_')}_{start}_to_{end}"
    folder.mkdir(parents=True, exist_ok=True)
    return folder
