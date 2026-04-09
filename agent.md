# Dataset Metadata Tool

A Gradio-based form for creating structured metadata for research datasets in concrete technology.

---

## Project Structure

```
metadata_tool/
├── app.py                      ← Entry point
├── config.py                   ← Paths, encodings, Gradio launch settings
├── data_loader.py              ← Loads CSVs + builds lookup maps
├── models.py                   ← Pydantic models & Datatype enum
├── state.py                    ← Global session state
├── requirements.txt
├── data/
│   ├── Materials.CSV
│   ├── Experiments.CSV
│   └── Data_Categories.CSV
├── handlers/
│   ├── author.py               ← Author form submission
│   ├── dataset.py              ← Dataset form submission
│   ├── experiments.py          ← Experiment dropdown helpers
│   ├── materials.py            ← Materials dropdown helpers
│   ├── data_categories.py      ← Data-category & column-description helpers
│   └── export.py               ← JSON export / save / clear
└── ui/
    └── layout.py               ← Gradio Blocks UI definition
```

---

## Running Locally

```bash
pip install -r requirements.txt
python app.py
```

Open http://localhost:7860 in your browser.

To enable the public share tunnel:
```bash
GRADIO_SHARE=true python app.py
```

---

## Deploying to HuggingFace Spaces

1. Create a new Space (SDK: **Gradio**).
2. Upload all files keeping the same folder layout.
3. Make sure `data/Materials.CSV`, `data/Experiments.CSV`, and
   `data/Data_Categories.CSV` are included in the repo.
4. HuggingFace automatically runs `app.py`; the `server_name="0.0.0.0"`
   setting in `config.py` makes the app accessible from outside.

### CSV path overrides (optional)

If you prefer to store the CSV files elsewhere, set these environment
variables in your Space settings:

| Variable              | Default                     |
|-----------------------|-----------------------------|
| `MATERIALS_CSV`       | `data/Materials.CSV`        |
| `EXPERIMENTS_CSV`     | `data/Experiments.CSV`      |
| `DATA_CATEGORIES_CSV` | `data/Data_Categories.CSV`  |

---

## Encodings

| File                  | Encoding |
|-----------------------|----------|
| `Materials.CSV`       | ASCII    |
| `Experiments.CSV`     | ASCII    |
| `Data_Categories.CSV` | UTF-16   |

Change these in `config.py` if your files use a different encoding.
