import streamlit as st
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore
import requests


BACKEND_URL = 'http://127.0.0.1:5000'
session  = st.session_state

if 'loggedIn' not in session:
    session.loggedIn = False
    st.switch_page("pages/login.py")
    
if session['loggedIn'] == False:
    st.switch_page("pages/login.py")


def connect(file):
    if file == "a":
        print("apples")
        
        return
    data = pd.read_csv("names.csv")
    
    data = data.rename(columns={'zp_xVJ20': 'Owner Name',
                                'zp-link href': 'Owner LinkedIn',
                                'zp_xVJ20 href': 'Apollo Link',
                                'zp_Y6y8d 2': 'Location',
                                'zp_Y6y8d 3': 'Number of Employees',
                                'zp_Y6y8d': 'Role', 
                                'zp_WM8e5': 'Company Name', 
                                'zp_IL7J9 src': 'Logo', 
                                'zp-link href 2': 'Website',
                                'zp-link href 3': 'Company LinkedIn',
                                'zp-link href 4': 'Facebook',
                                'zp_WM8e5 href': 'Owner Apollo',
                                'zp-link href 5': 'Twitter',
                                'zp-link': 'Email'
                               })
    
    data = data.rename(columns={'zp_PHqgZ': 'Data 1',
                                'zp_yc3J_': 'Data 2',
                                'zp_yc3J_ 2': 'Data 3',
                                'zp_yc3J_ 3': 'Data 4',
                                'zp_yc3J_ 4': 'Data 5',
                                'zp_yc3J_ 5': 'Data 6',
                                'zp_yc3J_ 6': 'Data 7',
                                'zp_yc3J_ 7': 'Data 8',
                                'zp_yc3J_ 8': 'Data 9',
                                'zp_yc3J_ 9': 'Data 10',
                                'zp_yc3J_ 10': 'Data 11',
                                'zp_yc3J_ 11': 'Data 12',
                                'zp_yc3J_ 12': 'Data 13',
                                'zp_yc3J_ 13': 'Data 14',
                                'zp_yc3J_ 14': 'Data 15',
                                'zp_lm1kV': 'Data 16'
                               })
    
    

    return data





def display_df(filepath):
    df = pd.read_csv(filepath)
    st.dataframe(df)



def title():
    col1, mid, col2 = st.columns([0.6,0.5,20], gap="medium")
    with col1:
        st.image("images/logo.png", width=77)
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
        page_icon="images/logo.png",
        layout="wide",
        #have the intial siberbar state as not expanded
        initial_sidebar_state="collapsed"
    )




title()





import os

uploaded_file = st.file_uploader("Upload Leads (.CSV)")
upload_button = st.button("Upload")

if upload_button:
    if uploaded_file is not None:
        #save the file in the filesystem as temp.csv
        with open('temp.csv', 'wb') as f:
            f.write(uploaded_file.getvalue())
            #send the file to the backend
            response = session.flask_session.post(f'{BACKEND_URL}/upload', files={'file': open('temp.csv', 'rb')})
            st.write(response.text)
            #remove the file from the filesystem
            os.remove('temp.csv')
    else:
        st.write("Please upload a file")