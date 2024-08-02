from selenium import webdriver
from selenium.webdriver.common.by import By
from openai import OpenAI
import base64
import os

os.environ["OPENAI_API_KEY"] = "sk-proj-IB5zqbtu2ZQDUepOueMhT3BlbkFJNRp1gsrsjlR5DPwY4VEs"
# Importing the Keys class from selenium
from selenium.webdriver.common.keys import Keys
import time
email= "pranavdesu@gmail.com" # Email ID of the sender
password= "Kw^2s;kB&X=_kFc" # Password of the sender
user = "Pranav Desu" # Name of the sender/ Name seen on LinkedIn


# Creating a webdriver instance
driver = webdriver.Edge()
# This instance will be used to log into LinkedIn
 
# Opening linkedIn's login page
driver.get("https://linkedin.com/login")
 
# waiting for the page to load
time.sleep(5)
 
# entering username
username = driver.find_element(By.ID, "username")
 
# In case of an error, try changing the element
# tag used here.
 
# Enter Your Email Address
username.send_keys(email)  
 
# entering password
pword = driver.find_element(By.ID, "password")
# In case of an error, try changing the element 
# tag used here.
 
# Enter Your Password
pword.send_keys(password)        

time.sleep(5)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(30)

# Open the webpage
driver.get("https://www.linkedin.com/in/akrit-agrawal/")

time.sleep(30)

# Take a screenshot and save it as 'screenshot.png'
driver.save_screenshot("screenshot.png")

# Quit the WebDriver session
driver.quit()


#Open AI

client = OpenAI()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

base64_image = encode_image('screenshot.png')

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "Your goal is to provide context about the company/person you're viewing, try to summarize everything the company does as simply as you can, usually around 1-2 sentences. Your answer should be in the following format: (first name), (role at company), (company name), (All other relevant context)."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/png;base64,{base64_image}"
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "Akrit, CEO, AiME Technologies. Akrit Agrawal is an entrepreneur leading AiME Technologies, a company focused on transforming innovative ideas into successful ventures."
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content)