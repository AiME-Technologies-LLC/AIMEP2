import numpy as np
import pandas as pd
from flask import Flask, session
from flask import request
import openai
from firebase import FirebaseHandler as fb
from flask_session import Session
import bcrypt
import json


def csv_to_json(file_path):
    data = pd.read_csv(file_path)
    j = data.to_json(orient='records')
    # to dict
    return json.loads(j)




def openai(message): 
    messages = [ {"role": "system", 
                  
                  "content": 
                  "You are a salesman designed for outreach. The message you will recieve will outline characteristics of a potential client." 
                 }]

    chat = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages )
    
    reply = chat.choices[0].message.content
    
    messages.append({"role": "assistant", "content": reply})
    
    return reply

def encrypt(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def  check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

#app = Flask(__name__)

#@app.route('/GPT3Response/rizz/', methods=['GET'])

app = Flask(__name__)
app.secret_key  = "secret"
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = True
Session(app)


firebase = fb('serviceAccount.json')


@app.route('/', methods=['GET', 'POST'])
def setSession():
    session["email"] = ''
    session['password'] = ''
    session['logged_in'] = False
    return 'Session set.'

@app.route('/checkSession', methods=['GET'])
def checkSession():
    return str(session.get('email', 'Not set'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    data = None
    if request.method == 'POST':
        data = request.get_json()
        if data is None:
            return 'No data received.'
        else:
            if firebase.check_document_exists('users', data['email']):
                return 'User already exists.'
            else:
                data['password'] = encrypt(data['password'])
                firebase.addDocument('users', data['email'], {'email': data['email'], 'password': data['password']})
                return 'User created successfully.'
    return 'Invalid request.'

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = None
    if request.method == 'POST':
        data = request.get_json()
        if data is None:
            return 'No data received.'
        else: 
            if session['logged_in']:
                return 'User already logged in.'
            if firebase.check_document_exists('users', data['email']):
                if check_password(data['password'], firebase.getFeild('users', data['email'], 'password')):
                    session['email'] = data['email']
                    session['password'] = data['password']
                    session['logged_in'] = True
                    return 'Login successful.'
                else:
                    return 'Incorrect password.'
            else:
                return 'User does not exist.'
    return 'Invalid request.'

@app.route('/uploadLeads', methods=['GET', 'POST'])
def uploadLeads():
    data = None
    if request.method == 'POST':
        file = request.files['file']
        if file is None:
            return 'No data received.'
        # check if user is logged in
        if not session['logged_in'] or session['email'] is None or session['password'] is None:
            return 'User not logged in.'
        
            

        else:
            data = csv_to_json(file)
            # print the length of the data
            print(len(data))
            for lead in data:
                # Check if the lead already exists with path to leads users/<email>/leads/<lead_name>
                print(lead['Email'])
                if firebase.check_document_exists(f"users/{session['email']}/leads", lead['Email']):
                    return 'Lead already exists.'
                firebase.addDocument(f"users/{session['email']}/leads", lead['Email'], lead)
            return 'Leads uploaded successfully.'
    return 'Invalid request.'

app.run('',port=5000)



    