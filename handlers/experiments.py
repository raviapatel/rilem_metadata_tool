"""
handlers/experiments.py
-----------------------
Helpers for the Experiment Selection section.
"""

import gradio as gr
import data_loader


def update_subs(category: str) -> tuple:
    """Populate sub-experiment dropdown when a category is selected."""
    if category not in data_loader.experiment_map:
        return gr.update(choices=[], value=[]), ""
    subs = sorted(set(data_loader.experiment_map[category]["subcategories"]))
    desc = data_loader.experiment_map[category]["description"]
    return gr.update(choices=subs, value=[]), desc


def add_experiment(category: str, subcategories: list, state: list) -> tuple[list, str]:
    """Append selected experiments to the running state list."""
    state = state or []
    if not category or not subcategories:
        return state, "⚠️ Select a category and at least one subcategory."
    for sub in subcategories:
        entry = f"{category} → {sub}"
        if entry not in state:
            state.append(entry)
    return state, ", ".join(state)
