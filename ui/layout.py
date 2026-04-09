"""
ui/layout.py
------------
Defines and returns the Gradio Blocks application.
All business logic lives in handlers/; this file only wires up widgets.
"""

import gradio as gr

import data_loader
from models import Datatype

from handlers.author import submit_author
from handlers.dataset import submit_dataset
from handlers.experiments import update_subs, add_experiment
from handlers.materials import update_materials, add_material
from handlers.data_categories import (
    update_data_subcategories,
    update_common_units,
    add_data_category,
    update_data_subcategories_for_columns,
    add_column_description,
)
from handlers.export import export_json, save_json_file, clear_all


def build_app() -> gr.Blocks:
    """Construct and return the Gradio Blocks app (not launched here)."""

    with gr.Blocks(title="Dataset Metadata Tool") as app:

        # ------------------------------------------------------------------ #
        #  Author Information                                                  #
        # ------------------------------------------------------------------ #
        gr.Markdown("## 🧾 Author Information")

        with gr.Row():
            title = gr.Textbox(label="Title", info="Title of the dataset")
            keywords = gr.Textbox(
                label="Keywords",
                info="Keywords related to the dataset (separate using commas)",
            )

        description_auth = gr.Textbox(
            label="Description", lines=3, info="Description of the dataset"
        )

        with gr.Row():
            uploader = gr.Textbox(
                label="Uploaded by",
                info="Name of the person who uploaded the dataset (First Name, Last Name)",
            )
            email = gr.Textbox(
                label="Email", info="Email of the person who uploaded the dataset"
            )

        with gr.Row():
            date = gr.Textbox(label="Date (YYYY-MM-DD)", info="Date of data creation")
            identifier = gr.Textbox(
                label="Identifier", info="Unique identifier for the dataset"
            )

        contributors = gr.Textbox(
            label="Contributors",
            info="Contributors (First Name 1, Last Name 1; First Name 2, Last Name 2 …)",
        )

        btn_auth = gr.Button("Submit Author")
        msg_auth = gr.Textbox(label="Author Status", interactive=False)
        js_auth = gr.JSON(label="Author Data")

        btn_auth.click(
            submit_author,
            [title, keywords, description_auth, uploader, email, date, identifier, contributors],
            [msg_auth, js_auth],
        )

        # ------------------------------------------------------------------ #
        #  Dataset Information                                                 #
        # ------------------------------------------------------------------ #
        gr.Markdown("## 📦 Dataset Information")

        dtype = gr.Dropdown([d.value for d in Datatype], label="Dataset Type")
        ext = gr.Textbox(label="File Extension")
        ts = gr.Checkbox(label="Time Series?")
        nfiles = gr.Number(label="Number of Files", value=1)
        desc_ds = gr.Textbox(label="Dataset Description", lines=3)

        # -- Column Descriptions (text/tables only) -------------------------
        with gr.Group(visible=False) as column_description_group:
            gr.Markdown("### 📑 Column Descriptions (only for Text / Tables)")

            col_super_cat = gr.Dropdown(
                list(data_loader.data_categories_map.keys()),
                label="Column Super Category",
            )
            col_sub = gr.Dropdown([], label="Column Data Subcategories", multiselect=True)
            col_desc_note = gr.Textbox(
                label="Category Description", interactive=False
            )
            col_name = gr.Textbox(label="Column Name (free text)")
            col_entity = gr.Textbox(label="Column Entity (free text)")

            btn_add_col = gr.Button("Add Column Description")
            col_display_box = gr.Textbox(
                label="Column Description List", lines=6, interactive=False
            )
            col_desc_state = gr.State([])

            col_super_cat.change(
                update_data_subcategories_for_columns,
                [col_super_cat],
                [col_sub, col_desc_note],
            )
            btn_add_col.click(
                add_column_description,
                [col_super_cat, col_sub, col_name, col_entity, col_desc_state],
                [col_desc_state, col_display_box],
            )

        # -- Global Data Categories ----------------------------------------
        with gr.Group(visible=True) as global_data_categories_group:
            gr.Markdown("### 🗂️ Data Categories (global)")

            data_super_cat = gr.Dropdown(
                list(data_loader.data_categories_map.keys()),
                label="Super Category",
            )
            data_cat_sub = gr.Dropdown(
                [], label="Data Category", multiselect=True
            )
            data_units = gr.Textbox(label="Common Units", interactive=False)

            btn_add_data_cat = gr.Button("Add Data Category")
            data_selected_box = gr.Textbox(
                label="Selected Data Categories", lines=4, interactive=False
            )
            data_cat_state = gr.State([])

            data_super_cat.change(
                update_data_subcategories,
                [data_super_cat],
                [data_cat_sub, data_units],
            )
            data_cat_sub.change(
                update_common_units,
                [data_cat_sub, data_super_cat],
                [data_units],
            )
            btn_add_data_cat.click(
                add_data_category,
                [data_super_cat, data_cat_sub, data_cat_state],
                [data_cat_state, data_selected_box],
            )

        # -- Materials -------------------------------------------------------
        gr.Markdown("### 🧱 Materials Selection")

        mat_cat = gr.Dropdown(
            list(data_loader.materials_map.keys()), label="Material Category"
        )
        mat_sub = gr.Dropdown([], label="Materials", multiselect=True)
        mat_desc = gr.Textbox(label="Category Description", interactive=False)

        btn_add_mat = gr.Button("Add Material(s)")
        mat_selected_box = gr.Textbox(
            label="Selected Materials", lines=4, interactive=False
        )
        mat_state = gr.State([])

        mat_cat.change(update_materials, [mat_cat], [mat_sub, mat_desc])
        btn_add_mat.click(
            add_material, [mat_cat, mat_sub, mat_state], [mat_state, mat_selected_box]
        )

        # -- Experiments -----------------------------------------------------
        gr.Markdown("### 🔬 Experiment Selection")

        exp_cat = gr.Dropdown(
            list(data_loader.experiment_map.keys()), label="Experiment Category"
        )
        exp_sub = gr.Dropdown([], label="Sub-Experiments", multiselect=True)
        exp_desc = gr.Textbox(label="Category Description", interactive=False)

        btn_add_exp = gr.Button("Add Experiment(s)")
        exp_selected_box = gr.Textbox(
            label="Selected Experiments", lines=6, interactive=False
        )
        exp_state = gr.State([])

        exp_cat.change(update_subs, [exp_cat], [exp_sub, exp_desc])
        btn_add_exp.click(
            add_experiment,
            [exp_cat, exp_sub, exp_state],
            [exp_state, exp_selected_box],
        )

        # -- Temperature -----------------------------------------------------
        gr.Markdown("### 🌡️ Temperature Data")

        temp_source = gr.Dropdown(
            ["none", "in the dataset", "Room Temperature", "user defined"],
            label="Temperature Source",
        )
        temp_value = gr.Number(label="Value", visible=False)
        temp_unit = gr.Dropdown(["°C", "°F", "°K"], label="Unit", visible=False)

        def toggle_temp_fields(source):
            show = source == "user defined"
            return gr.update(visible=show), gr.update(visible=show)

        temp_source.change(
            toggle_temp_fields, [temp_source], [temp_value, temp_unit]
        )

        # -- Location --------------------------------------------------------
        gr.Markdown("### 🗺️ Location Data")

        location_source = gr.Dropdown(
            ["none", "in the dataset", "Laboratory/Indoor", "Coordinates"],
            label="Location Source",
        )
        location_value = gr.Textbox(label="Coordinates", visible=False)

        def toggle_location_fields(source):
            return gr.update(visible=source == "Coordinates")

        location_source.change(
            toggle_location_fields, [location_source], [location_value]
        )

        # -- dtype toggle (nfiles / column descriptions / global data cats) --
        def toggle_fields_for_dtype(dtype_val):
            is_text = dtype_val == "text/tables"
            return (
                gr.update(visible=not is_text),   # nfiles
                gr.update(visible=is_text),        # column_description_group
                gr.update(visible=not is_text),    # global_data_categories_group
            )

        dtype.change(
            toggle_fields_for_dtype,
            [dtype],
            [nfiles, column_description_group, global_data_categories_group],
        )

        # -- Submit dataset --------------------------------------------------
        btn_ds = gr.Button("Submit Dataset Metadata")
        ds_status = gr.Textbox(label="Status", interactive=False)
        ds_json = gr.JSON(label="Dataset Metadata")

        btn_ds.click(
            submit_dataset,
            [
                dtype, ext, ts, nfiles, desc_ds,
                data_cat_state, mat_state, exp_state,
                temp_source, temp_value, temp_unit,
                location_source, location_value,
                col_desc_state,
            ],
            [ds_status, ds_json],
        )

        # ------------------------------------------------------------------ #
        #  Export                                                              #
        # ------------------------------------------------------------------ #
        gr.Markdown("### 💾 Export")

        btn_export = gr.Button("Generate Combined JSON")
        combined_json = gr.Textbox(label="Combined JSON", lines=8)
        export_status = gr.Textbox(label="Export Status", interactive=False)
        btn_export.click(export_json, [], [combined_json, export_status])

        btn_save = gr.Button("Save JSON")
        download_file = gr.File(label="Download JSON")
        btn_save.click(save_json_file, [], [download_file, export_status])

        # ------------------------------------------------------------------ #
        #  Clear                                                               #
        # ------------------------------------------------------------------ #
        gr.Markdown("---")
        btn_clear = gr.Button("🧹 Clear All")
        btn_clear.click(
            clear_all,
            [],
            [
                export_status,
                js_auth,
                combined_json,
                exp_selected_box,
                msg_auth,
                data_selected_box,
                col_display_box,
            ],
        )

    return app
