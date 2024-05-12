import numpy as np
import pandas as pd
from flask import Flask
import openai

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

def openai(message): 
    messages = [ {"role": "system", 
                  
                  "content": 
                  "You are a salesman designed for outreach. The message you will recieve will outline characteristics of a potential client." 
                 }]

    chat = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages )
    
    reply = chat.choices[0].message.content
    
    messages.append({"role": "assistant", "content": reply})
    
    return reply
#app = Flask(__name__)
#app.run(debug=False)

#@app.route('/GPT3Response/rizz/', methods=['GET'])