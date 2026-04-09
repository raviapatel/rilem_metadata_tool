"""
handlers/dataset.py
-------------------
Handles the Dataset Information form submission.
"""

import traceback

import state
from models import Datatype


def _enum_from_value(enum_type, val):
    """Look up an enum member by value or name."""
    if val is None:
        return None
    if isinstance(val, enum_type):
        return val
    for member in enum_type:
        if str(member.value) == str(val) or str(member.name) == str(val):
            return member
    raise ValueError(f"Value '{val}' not found in enum {enum_type.__name__}")


def submit_dataset(
    dtype: str,
    ext: str,
    ts: bool,
    nfiles,
    desc: str,
    data_cats_selected: list,
    materials_selected: list,
    exps: list,
    temp_source: str,
    temp_value,
    temp_unit: str,
    location_source: str,
    location_value: str,
    column_desc_state: list,
) -> tuple[str, dict]:
    """
    Validate and store one dataset metadata block.

    Returns
    -------
    (status_message, dataset_entry_dict)
    """
    try:
        if dtype in (None, ""):
            return "❌ Dataset type is required.", {}
        if not ext:
            return "❌ File extension is required.", {}

        dtype_member = _enum_from_value(Datatype, dtype)

        # text/tables always counts as 1 file
        if dtype == "text/tables":
            file_count = 1
        else:
            try:
                file_count = int(nfiles)
            except Exception:
                return "❌ Number of files must be an integer.", {}

        # Temperature
        temp_entry = None
        if temp_source and temp_source != "none":
            temp_entry = (
                {"value": temp_value, "unit": temp_unit}
                if temp_source == "user defined"
                else temp_source
            )

        # Location
        loc_entry = None
        if location_source and location_source != "none":
            loc_entry = (
                location_value
                if location_source == "Coordinates"
                else location_source
            )

        dataset_entry = {
            "pick_dataset_type": dtype_member.value,
            "extension_of_the_file": str(ext),
            "time_series": bool(ts),
            "number_of_files": file_count,
            "description": str(desc),
            "Data_Categories": data_cats_selected or [],
            "Materials": materials_selected or [],
            "Experiments": exps or [],
            "Temperature_Data": temp_entry,
            "Location_Data": loc_entry,
            "Column_Descriptions": column_desc_state or [],
        }

        state.dataset_form_data.append(dataset_entry)
        return "✅ Dataset metadata submitted!", dataset_entry

    except Exception as exc:
        tb = traceback.format_exc()
        return f"❌ Error submitting dataset: {type(exc).__name__}: {exc}\n{tb}", {}
