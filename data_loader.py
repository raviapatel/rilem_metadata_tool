"""
data_loader.py
--------------
Loads the three reference CSV files and builds the lookup maps used
throughout the application.  Call `load_all()` once at startup.
"""

import pandas as pd
from config import (
    MATERIALS_CSV, EXPERIMENTS_CSV, DATA_CATEGORIES_CSV,
    MATERIALS_ENCODING, EXPERIMENTS_ENCODING, DATA_CATEGORIES_ENCODING,
)


# --------------------------------------------------------------------------- #
#  Raw DataFrames (populated by load_all)                                      #
# --------------------------------------------------------------------------- #
materials_df: pd.DataFrame = pd.DataFrame()
experiments_df: pd.DataFrame = pd.DataFrame()
data_categories_df: pd.DataFrame = pd.DataFrame()

# --------------------------------------------------------------------------- #
#  Lookup maps (populated by load_all)                                         #
# --------------------------------------------------------------------------- #
# { category_name: {"description": str, "materials": [str, ...]} }
materials_map: dict = {}

# { experiment_type: {"description": str, "subcategories": [str, ...]} }
experiment_map: dict = {}

# { super_category: {"description": str, "subcategories": [{"name": str, "units": str}, ...]} }
data_categories_map: dict = {}


def load_all() -> None:
    """Load CSVs and build all lookup maps.  Raises FileNotFoundError if a CSV
    is missing so the caller gets a clear error message."""
    global materials_df, experiments_df, data_categories_df
    global materials_map, experiment_map, data_categories_map

    # --- Load ---
    materials_df = pd.read_csv(MATERIALS_CSV, encoding=MATERIALS_ENCODING)
    experiments_df = pd.read_csv(EXPERIMENTS_CSV, encoding=EXPERIMENTS_ENCODING)
    data_categories_df = pd.read_csv(DATA_CATEGORIES_CSV, encoding=DATA_CATEGORIES_ENCODING)

    # Normalise experiments column names
    experiments_df.columns = ["Experiment_Type", "Experiment_Description", "Common_Experiment"]

    # --- Build experiment map ---
    experiment_map.clear()
    for _, row in experiments_df.iterrows():
        cat = str(row["Experiment_Type"]).strip()
        desc = str(row["Experiment_Description"]).strip()
        sub = str(row["Common_Experiment"]).strip()
        if cat not in experiment_map:
            experiment_map[cat] = {"description": desc, "subcategories": []}
        experiment_map[cat]["subcategories"].append(sub)

    # --- Build materials map ---
    materials_map.clear()
    for _, row in materials_df.iterrows():
        mat = str(row["Material"]).strip()
        cat = str(row["Category"]).strip()
        desc = str(row["Description"]).strip()
        if cat not in materials_map:
            materials_map[cat] = {"description": desc, "materials": []}
        materials_map[cat]["materials"].append(mat)

    # --- Build data-categories map ---
    data_categories_map.clear()
    for _, row in data_categories_df.iterrows():
        super_cat = str(row["Super_Category"]).strip()
        data_cat = str(row["Data_Category"]).strip()
        units = str(row["Common_Units"]).strip()
        desc = str(row.get("Description", "")).strip() if "Description" in data_categories_df.columns else ""
        if super_cat not in data_categories_map:
            data_categories_map[super_cat] = {"description": super_cat, "subcategories": []}
        data_categories_map[super_cat]["subcategories"].append({"name": data_cat, "units": units, "description": desc})

    print("✅ CSVs loaded successfully.")
    print(f"   Materials categories : {len(materials_map)}")
    print(f"   Experiment types     : {len(experiment_map)}")
    print(f"   Data super-categories: {len(data_categories_map)}")
