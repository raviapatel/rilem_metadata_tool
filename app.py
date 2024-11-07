import streamlit as st
from tabs import homepage, page, investigation , material # Importing the page modules

# Dictionary of pages
pages = {
    "Home": homepage.show,
    "page": page.display_and_download,
    "investigator_form": investigation.investigator_form,
    "material": material.main,
}

def main():
    st.sidebar.title('Navigation')  # This will add a title to the sidebar called "Navigation"
    selection = st.sidebar.radio("Choose a page:", list(pages.keys()))  # Radio buttons for page selection

    # Execute the function associated with the chosen page
    pages[selection]()

if __name__ == "__main__":
    main()

#### test writing tanja
