"""
config.py
---------
Central configuration for file paths and encodings.

Works on:
  - Local machine  →  CSV files sit next to this project, or set env vars below.
  - HuggingFace Spaces  →  Upload the three CSV files into the repo root (alongside app.py).

Override any path by setting environment variables before launching:
    export MATERIALS_CSV=/path/to/Materials.CSV
    export EXPERIMENTS_CSV=/path/to/Experiments.CSV
    export DATA_CATEGORIES_CSV=/path/to/Data_Categories.CSV
"""

import os
from pathlib import Path

# Root of the project (the folder that contains config.py)
BASE_DIR = Path(__file__).parent

# --------------------------------------------------------------------------- #
#  CSV file locations                                                          #
# --------------------------------------------------------------------------- #
MATERIALS_CSV = Path(os.getenv("MATERIALS_CSV", BASE_DIR / "assets" / "Materials.CSV"))
EXPERIMENTS_CSV = Path(os.getenv("EXPERIMENTS_CSV", BASE_DIR / "assets" / "Experiments.CSV"))
DATA_CATEGORIES_CSV = Path(os.getenv("DATA_CATEGORIES_CSV", BASE_DIR / "assets" / "Data_Categories.CSV"))

# --------------------------------------------------------------------------- #
#  CSV encodings                                                               #
# --------------------------------------------------------------------------- #
MATERIALS_ENCODING = "ascii"
EXPERIMENTS_ENCODING = "ascii"
DATA_CATEGORIES_ENCODING = "UTF-16"

# --------------------------------------------------------------------------- #
#  Gradio launch settings                                                      #
# --------------------------------------------------------------------------- #
# HuggingFace Spaces requires server_name="0.0.0.0" and share=False.
# Locally you can use share=True or the default 127.0.0.1.
# Auto-detect: HF Spaces sets the SPACE_ID env var.
_ON_HF_SPACES = os.getenv("SPACE_ID") is not None
SERVER_NAME = os.getenv("GRADIO_SERVER_NAME", "0.0.0.0" if _ON_HF_SPACES else "127.0.0.1")
SERVER_PORT = int(os.getenv("GRADIO_SERVER_PORT", 7860))
SHARE = os.getenv("GRADIO_SHARE", "false").lower() == "true"
DEBUG = os.getenv("GRADIO_DEBUG", "false").lower() == "true"
