import streamlit as st
import pandas as pd
import requests

def display_df(filepath):
    df = pd.read_csv(filepath)
    st.dataframe(df)
    
session = st.session_state


s = requests.Session()
s.headers.update({'Content-Type': 'application/json'})
BACKEND_URL = 'http://127.0.0.1:5000'
print(s.get(BACKEND_URL).text)

if 'loggedIn' not in session:
    session.loggedIn = False


def fetch_login(user, password):
    #send a post to localhost:5000/login
    #return the response
        

    
    response = s.post(f'{BACKEND_URL}/login', json={"email": user, "password": password})
    return response.text


def login():

    # Create an empty container
    placeholder = st.empty()
    

    # Insert a form in the container
    with placeholder.form("login"):
        st.markdown("#### Enter your credentials")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
    
    
    if submit:
        if email == "" or password == "":
            st.error("Please fill in both fields.")
        elif ltry:=fetch_login(email, password) == "Login successful.":
            # If the form is submitted and the email and password are correct,
            # clear the form/container and display a success message
            placeholder.empty()
            st.success("Login successful")
            session.loggedIn = True
            session.flask_session = s
            st.switch_page("app.py")
        
        elif  not ltry == "Login successful.":
            st.error(ltry)
    else:
        pass



st.set_page_config(
        page_title="AIME",
        page_icon="FrontEnd\images\logo.png",
        layout="wide",
        initial_sidebar_state="collapsed"
    )





login()











    