"""
handlers/materials.py
---------------------
Helpers for the Materials Selection section.
"""

import gradio as gr
import data_loader


def update_materials(category: str) -> tuple:
    """Populate materials dropdown when a category is selected."""
    if category not in data_loader.materials_map:
        return gr.update(choices=[], value=[]), ""
    mats = sorted(set(data_loader.materials_map[category]["materials"]))
    desc = data_loader.materials_map[category]["description"]
    return gr.update(choices=mats, value=[]), desc


def add_material(category: str, mats: list, state: list) -> tuple[list, str]:
    """Append selected materials to the running state list."""
    state = state or []
    if not category or not mats:
        return state, "⚠️ Select a category and at least one material."
    for m in mats:
        entry = f"{category} → {m}"
        if entry not in state:
            state.append(entry)
    return state, ", ".join(state)
