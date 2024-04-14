import streamlit as st
import pandas as pd

def display_df(filepath):
    df = pd.read_csv(filepath)
    st.dataframe(df)



def title():
    col1, mid, col2 = st.columns([0.6,0.5,20], gap="medium")
    with col1:
        st.image('FrontEnd\images\logo.png', width=77)
    with mid:
        st.write("  ")
    with col2:
        st.title("AIME")
    st.subheader("Upload Lead Files")

    
def addComptoSideBar(comp):
    with st.sidebar:
        comp1 = comp

st.set_page_config(
        page_title="AIME",
        page_icon="FrontEnd\images\logo.png",
        layout="wide",
        initial_sidebar_state="expanded"
    )





title()






uploaded_file = st.file_uploader("Upload Leads (.CSV)")

if uploaded_file is not None:
    try:
        # Check the file extension to use the correct pandas function
        if uploaded_file.name.endswith('.csv'):
            # For CSV files
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            # For Excel files
            df = pd.read_excel(uploaded_file)

        # Display the dataframe
        st.write(df)
    except Exception as e:
        st.write("Error reading file:", e)







    