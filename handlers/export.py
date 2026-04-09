"""
handlers/export.py
------------------
JSON export, file save, and session-clear handlers.
"""

import json

import gradio as gr

import state


def export_json() -> tuple[str, str]:
    """Combine author and dataset data into a single JSON string."""
    if not state.author_data and not state.dataset_form_data:
        return "", "⚠️ No data to export yet."

    combined = {}
    if state.author_data:
        combined["Author_Info"] = state.author_data
    if state.dataset_form_data:
        combined["Datasets"] = state.dataset_form_data

    js = json.dumps(combined, indent=2, default=str)
    return js, "⚡ Combined JSON prepared."


def save_json_file() -> tuple:
    """Write the combined JSON to disk and return a gr.File download object."""
    js, msg = export_json()
    if not js:
        return None, msg
    fname = "form_data.json"
    with open(fname, "w", encoding="utf-8") as fh:
        fh.write(js)
    return fname, "💾 JSON written to form_data.json"


def clear_all() -> tuple:
    """Reset all global state and return Gradio update objects."""
    state.reset()
    return (
        gr.update(value="Data cleared."),   # export_status
        gr.update(value={}),                # js_auth
        gr.update(value=""),                # combined_json
        gr.update(value=""),                # exp_selected_box
        gr.update(value=""),                # msg_auth
        gr.update(value=""),                # data_selected_box
        gr.update(value=""),                # col_display_box
    )
