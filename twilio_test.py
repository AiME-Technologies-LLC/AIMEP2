import os
from twilio.rest import Client

account_sid = 'ACcec52275b4d16d69184ae20eaaff275d'
auth_token = '524dafe935807337065d55fb36020653'
client = Client(account_sid, auth_token)

message = client.messages.create(
                     from_ = '+18662837290',
                     body = "Hi, this is a test message for AiME Technologies",
                     to = '+16786205329' 
                 )
