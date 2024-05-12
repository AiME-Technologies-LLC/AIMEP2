import streamlit as st
import pandas as pd
import Apollo_flask
import firebase_admin
from firebase_admin import credentials, firestore

def read_firestore_database():
    docs = leads.stream()
    
    for doc in docs:
        print(f"Document ID: {doc.id}")
        print(f"Document Data: {doc.to_dict()}")
        print()

def edit_firestore_database(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        cleaned_df = Apollo_flask.connect(uploaded_file)
        
        data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "+1234567890"
        }
        
        leads.document("Test Successful").set(data)
        
        print("Data added successfully.")

cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred)
firestore_db = firestore.client()

user = firestore_db.collection("Users").document("@PranavDesu")
leads = user.collection("Leads")

def display_df(filepath):
    df = pd.read_csv(filepath)
    st.dataframe(df)



def title():
    col1, mid, col2 = st.columns([0.6,0.5,20], gap="medium")
    with col1:
        st.image('FrontEnd\images\logo.png', width=77)
        pass
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
            cleaned_df = Apollo_flask.connect(uploaded_file)
            
            data_list = ["Owner Name", "Apollo Link", "Owner LinkedIn", "Role", "Logo", "Company Name", "Owner Apollo",
                         "Website", "Company LinkedIn", "Facebook", "Twitter", "Location", "Number of Employees", "Email",
                         "Data 1", "Data 2", "Data 3", "Data 4", "Data 5", "Data 6", "Data 7", "Data 8", "Data 9", "Data 10",
                         "Data 11", "Data 12", "Data 13", "Data 14", "Data 15", "Data 16"]

            i = 0
            for index, row in cleaned_df.iterrows():
                data = {}
                for column in data_list:
                    
                    data[column] = row[column]
                leads.document(row["Company Name"]).set(data)
                i += 1
            
        elif uploaded_file.name.endswith('.xlsx'):
            # For Excel files
            df = pd.read_excel(uploaded_file)

        # Display the dataframe
        st.write(df)
        st.write(cleaned_df)
    except Exception as e:
        st.write("Error reading file:", e)
    
firebase_admin.delete_app(firebase_admin.get_app())