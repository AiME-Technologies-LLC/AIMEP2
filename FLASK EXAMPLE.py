from flask import Flask
from flask_restful import Api, Resource
import openai
import base64
from PIL import Image
import io
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import bcrypt
import numpy as np
import cv2
import time






openai.api_key = ''
def GPT3Rizz(message):
    messages = [ {"role": "system", "content": 

              "you are a wingman trying to help the user impress someone over text. The messages you will recive are messages from the special someone. Respond in the best way and remember to stay flirtatious,. Dont be formal give short responses. oen sentence"} ]

    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        print(messages)
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply
    

from flask import Flask, jsonify, request

app = Flask(__name__)
                                                                                 
db = {} # user : pass

@app.route('/GPT3Response/rizz/', methods=['GET'])
def getResponse():
    
    
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    return jsonify({'message': "hello"})



if __name__ == "__main__":
    app.run(debug=True)
    
    
######################################################################### seconf example

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5000 }
]


@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204