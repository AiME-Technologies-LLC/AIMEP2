import requests
session = requests.Session()
# send names.csv to this endpoint http://127.0.0.1:5000/login
url = 'http://127.0.0.1:5000/login'
url1 = 'http://127.0.0.1:5000/uploadLeads'
file_path = 'C:/Users/siddu/Desktop/Coding-adventures/AIME CODE/AIMEP2/names.csv'

email = "admin"
password = "admin"
session.get('http://127.0.0.1:5000/')
with open(file_path, 'rb') as f:
    response2 = session.post(url, json={'email': email, 'password': password})
    response1 = session.post(url1, files={'file': f})



print(response1.text)
print(response2.text)

# # import bcrypt
# # def encrypt(password):
# #     return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# # def  check_password(password, hashed):
# #     return bcrypt.checkpw(password.encode('utf-8'), hashed)

# # password = "passord"

# # hashed = encrypt("hello") 


# # print(check_password("hello", hashed))



import pandas as pd
# def connect(file):

#     data = pd.read_csv(file)
    
#     data = data.rename(columns={'zp_xVJ20': 'Owner Name',
#                                 'zp-link href': 'Owner LinkedIn',
#                                 'zp_xVJ20 href': 'Apollo Link',
#                                 'zp_Y6y8d 2': 'Location',
#                                 'zp_Y6y8d 3': 'Number of Employees',
#                                 'zp_Y6y8d': 'Role', 
#                                 'zp_WM8e5': 'Company Name', 
#                                 'zp_IL7J9 src': 'Logo', 
#                                 'zp-link href 2': 'Website',
#                                 'zp-link href 3': 'Company LinkedIn',
#                                 'zp-link href 4': 'Facebook',
#                                 'zp_WM8e5 href': 'Owner Apollo',
#                                 'zp-link href 5': 'Twitter',
#                                 'zp-link': 'Email'
#                                })
    
#     data = data.rename(columns={'zp_PHqgZ': 'Data 1',
#                                 'zp_yc3J_': 'Data 2',
#                                 'zp_yc3J_ 2': 'Data 3',
#                                 'zp_yc3J_ 3': 'Data 4',
#                                 'zp_yc3J_ 4': 'Data 5',
#                                 'zp_yc3J_ 5': 'Data 6',
#                                 'zp_yc3J_ 6': 'Data 7',
#                                 'zp_yc3J_ 7': 'Data 8',
#                                 'zp_yc3J_ 8': 'Data 9',
#                                 'zp_yc3J_ 9': 'Data 10',
#                                 'zp_yc3J_ 10': 'Data 11',
#                                 'zp_yc3J_ 11': 'Data 12',
#                                 'zp_yc3J_ 12': 'Data 13',
#                                 'zp_yc3J_ 13': 'Data 14',
#                                 'zp_yc3J_ 14': 'Data 15',
#                                 'zp_lm1kV': 'Data 16'
#                                })
    
    

#     return data

# # #convert the datafram to csv
# # data.to_csv('C:/Users/siddu/Desktop/Coding-adventures/AIME CODE/AIMEP2/names.csv', index=False)

# conver the csv to json
# data = pd.read_csv('C:/Users/siddu/Desktop/Coding-adventures/AIME CODE/AIMEP2/names.csv')
# data.to_json('C:/Users/siddu/Desktop/Coding-adventures/AIME CODE/AIMEP2/names.json', orient='records')

# import json

# my_file = open("C:/Users/siddu/Desktop/Coding-adventures/AIME CODE/AIMEP2/names.json", "r")
# loaded_json = json.load(my_file)

# #save the json file
# with open('C:/Users/siddu/Desktop/Coding-adventures/AIME CODE/AIMEP2/names.json', 'w') as f:
#     json.dump(loaded_json, f, indent=2)