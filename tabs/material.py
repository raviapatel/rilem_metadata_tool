import streamlit as st
import json

def main():
    st.title("Material Data Entry Form")

    with st.form("Material Form"):
        # Material main details
        st.subheader("Material Details")
        material_name = st.text_input("Name")
        material_type_name = st.text_input("Material Type")

        # MaterialParameters
        st.subheader("Material Parameters")
        param_count = st.number_input("Number of Material Parameters", min_value=0, step=1)
        material_parameters = []
        for _ in range(int(param_count)):
            param_name = st.text_input(f"Parameter Name", key=f"param_name_{_}")
            param_value = st.text_input(f"Parameter Value", key=f"param_value_{_}")
            material_parameters.append({"name": param_name, "value": param_value})

        # Composite details (if any)
        st.subheader("Composite Details")
        composite_name = st.text_input("Composite Name")
        composite_type = st.text_input("Composite Type")
        
        # Materials in Composite
        materials_in_composite = st.text_area("List of materials in Composite (comma-separated)")

        # Fraction of each material in the composite
        fractions = st.text_area("Fraction of each material (comma-separated)")

        # Submit button
        submitted = st.form_submit_button("Submit")

    if submitted:
        material_data = {
            "Material": {
                "name": material_name,
                "type": material_type_name,
                "parameters": material_parameters
            },
            "Composite": {
                "name": composite_name,
                "type": composite_type,
                "materials": materials_in_composite.split(","),
                "fractions": list(map(float, fractions.split(",")))
            }
        }

        # Convert to JSON
        json_str = json.dumps(material_data, indent=4)
        
        # Display the data (optional)
        st.write("Material Data as JSON:")
        st.json(material_data)

        # Download button for JSON
        st.download_button(label='Download JSON',
                           data=json_str,
                           file_name='material_data.json',
                           mime='application/json')
 