"""
app.py
------
Entry point.  Run locally with:

    python app.py

Deploy to HuggingFace Spaces by uploading this entire project folder.
The Space must include the three CSV files under data/:
    data/Materials.CSV
    data/Experiments.CSV
    data/Data_Categories.CSV

Environment variables (all optional):
    MATERIALS_CSV          – override CSV path
    EXPERIMENTS_CSV        – override CSV path
    DATA_CATEGORIES_CSV    – override CSV path
    GRADIO_SERVER_NAME     – default "0.0.0.0"
    GRADIO_SERVER_PORT     – default 7860
    GRADIO_SHARE           – "true" to enable a public tunnel (local only)
    GRADIO_DEBUG           – "true" to enable debug mode
"""

import warnings
warnings.filterwarnings("ignore")

# Load reference data before building the UI (maps must exist at import time
# of ui/layout.py because the dropdowns are populated at definition time).
import data_loader
data_loader.load_all()

from ui.layout import build_app
from config import SERVER_NAME, SERVER_PORT, SHARE, DEBUG

if __name__ == "__main__":
    app = build_app()
    app.queue()
    app.launch(
        server_name=SERVER_NAME,
        server_port=SERVER_PORT,
        share=SHARE,
        debug=DEBUG,
    )


