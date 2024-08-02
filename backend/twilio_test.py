
from twilio.rest import Client

account_sid = 'ACad30301d9bac4e7e64aeaa288523c423'
auth_token = '686c0076ba66592f71b70da211d6fc7c'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+18669412767',
                     to='+19452162299'
                 )

print(message.sid)