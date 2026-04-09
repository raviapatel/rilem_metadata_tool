"""
state.py
--------
Global mutable state for the current session.

NOTE: Gradio runs in a single process, so module-level globals work fine for
a single-user tool.  For multi-user HuggingFace deployments you would move
this state into Gradio's gr.State objects (already done for the list-type
states in the UI layer).  The dicts here are for cross-tab / cross-section
data that is assembled at export time.
"""

# Submitted author information (filled by submit_author handler)
author_data: dict = {}

# List of dataset metadata blocks (one per "Submit Dataset Metadata" click)
dataset_form_data: list = []


def reset() -> None:
    """Clear all session state – called by the Clear All button."""
    global author_data, dataset_form_data
    author_data.clear()
    dataset_form_data.clear()
