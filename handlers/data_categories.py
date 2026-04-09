"""
handlers/data_categories.py
----------------------------
Helpers for the global Data Categories section and the per-column
Data Subcategories section.
"""

import gradio as gr
import data_loader


# --------------------------------------------------------------------------- #
#  Global data categories                                                      #
# --------------------------------------------------------------------------- #

def update_data_subcategories(super_cat: str) -> tuple:
    """Populate sub-category dropdown for the global data-category picker."""
    if super_cat not in data_loader.data_categories_map:
        return gr.update(choices=[], value=[]), ""
    subs = [item["name"] for item in data_loader.data_categories_map[super_cat]["subcategories"]]
    return gr.update(choices=subs, value=[]), f"Super Category: {super_cat}"


def update_common_units(data_cats, super_cat: str):
    """Update the units textbox when a data subcategory is selected."""
    if not super_cat or not data_cats:
        return gr.update(value="")
    first_cat = data_cats[0] if isinstance(data_cats, list) else data_cats
    for item in data_loader.data_categories_map[super_cat]["subcategories"]:
        if item["name"] == first_cat:
            return gr.update(value=item["units"])
    return gr.update(value="")


def add_data_category(super_cat: str, data_cat, state: list) -> tuple[list, str]:
    """Append a data-category selection to the running state list."""
    state = state or []
    if not super_cat or not data_cat:
        return state, "⚠️ Select a super category and a data category."
    entry = f"{super_cat} → {data_cat}"
    if entry not in state:
        state.append(entry)
    return state, ", ".join(state)


# --------------------------------------------------------------------------- #
#  Per-column data subcategories (text/tables mode only)                       #
# --------------------------------------------------------------------------- #

def update_data_subcategories_for_columns(super_cat: str) -> tuple:
    """Same logic as the global version, kept separate for UI clarity."""
    if super_cat not in data_loader.data_categories_map:
        return gr.update(choices=[], value=[]), ""
    subs = [item["name"] for item in data_loader.data_categories_map[super_cat]["subcategories"]]
    return gr.update(choices=subs, value=[]), f"Super Category: {super_cat}"


def add_column_description(
    super_cat: str,
    data_subs: list,
    col_name: str,
    col_entity: str,
    state: list,
) -> tuple[list, str]:
    """
    Append a column description entry to the running state list.

    Each entry is a dict:
        { column_name, column_entity, super_category, data_subcategories }

    Returns (updated_state, formatted_display_text).
    """
    state = state or []
    if not col_name or not col_entity:
        return state, "⚠️ Please provide both Column Name and Column Entity."

    entry_obj = {
        "column_name": str(col_name),
        "column_entity": str(col_entity),
        "super_category": super_cat or "",
        "data_subcategories": data_subs or [],
    }

    if entry_obj not in state:
        state.append(entry_obj)

    lines = []
    for i, e in enumerate(state, start=1):
        sc_part = e["super_category"] or ""
        subs_part = ", ".join(e["data_subcategories"]) if e["data_subcategories"] else ""
        cat_part = f"{sc_part} → {subs_part}" if (sc_part or subs_part) else ""
        lines.append(f"{i} | {e['column_name']} | {e['column_entity']} | {cat_part}")

    return state, "\n".join(lines)
