import streamlit as st
import json
def investigator_form():
    st.title("Investigation Form")

    with st.form("Investigation Form"):
        # Investigation inputs
        st.subheader("Investigation Details")
        datasets = st.text_area("Enter datasets (comma-separated)")
        materials = st.selectbox("Materials", ["Material 1", "Material 2", "Material 3"])

        # Investigator inputs
        st.subheader("Investigator Details")
        investigator_name = st.text_input("Name")
        institutions = st.text_area("Institutions (comma-separated)")
        orcid = st.text_input("ORCID")
        credit_role = st.text_area("CREDIT roles (comma-separated)")

        # Corresponding author checkbox
        is_corresponding = st.checkbox("Is corresponding author?")

        # Publication inputs
        st.subheader("Publication Details")
        pub_title = st.text_input("Title")
        authors = st.text_area("Authors (comma-separated)")
        journal = st.text_input("Journal")
        doi = st.text_input("DOI")

        # Submit button
        submitted = st.form_submit_button("Submit")
    if submitted:
        # Create a dictionary with the data
        data = {
            "Investigation": {
                "datasets": datasets,
                "materials": st.dro
            },
            "Investigator": {
                "name": investigator_name,
                "institutions": institutions,
                "orcid": orcid,
                "credit_role": credit_role,
                "is_corresponding_author": is_corresponding
            },
            "Publication": {
                "title": pub_title,
                "authors": authors,
                "journal": journal,
                "doi": doi
            }
        }

        # Convert dictionary to JSON
        json_str = json.dumps(data, indent=4)
        
        # Create a download link for the JSON file
        st.download_button(label='Download JSON',
                           data=json_str,
                           file_name='investigation_data.json',
                           mime='application/json',
                           help='Click to download your data as a JSON file')
