import streamlit as st

import streamlit as st
import pandas as pd

def display_and_download():
    st.title('Data Entry and Download')

    # Determine the number of rows in the table
    n_rows = st.number_input('Enter the number of rows:', min_value=0, max_value=100, value=5)
    n_rows = int(n_rows)  # Ensure it's an integer

    # Create a dataframe with specified number of rows
    data = {
        "Number": range(1, n_rows + 1),
        "Text": [""] * n_rows  # Empty strings as placeholders
    }
    df = pd.DataFrame(data)

    # Use streamlit to allow user to input data in the 'Text' column
    for i in range(n_rows):
        df.at[i, 'Text'] = st.text_input(f"Row {i+1} Text", key=f"row_{i}_text")

    # Show the dataframe
    st.write(df)

    # Button to download the dataframe as a JSON file
    if st.button('Download JSON'):
        # Convert DataFrame to JSON
        json_str = df.to_json(orient='records', lines=False)
        # Create a download link
        st.download_button(label='Download JSON', data=json_str, file_name='table_data.json', mime='application/json')

