from selenium import webdriver
from selenium.webdriver.common.by import By
from openai import OpenAI
import base64
import os


# Importing the Keys class from selenium
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from openai import OpenAI
import base64
import os
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

# email = os.getenv("LINKEDIN_EMAIL")
# password = os.getenv("LINKEDIN_PASSWORD")

# # Creating a webdriver instance
# driver = webdriver.Edge()
# # This instance will be used to log into LinkedIn
 
# # Opening linkedIn's login page
# driver.get("https://linkedin.com/login")
 
# # waiting for the page to load
# time.sleep(5)
 
# # entering username
# username = driver.find_element(By.ID, "username")
 
# # In case of an error, try changing the element
# # tag used here.
 
# # Enter Your Email Address
# username.send_keys(email)  
 
# # entering password
# pword = driver.find_element(By.ID, "password")
# # In case of an error, try changing the element 
# # tag used here.
 
# # Enter Your Password
# pword.send_keys(password)        

# time.sleep(5)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(5)

# # Open the webpage
# driver.get("https://www.linkedin.com/in/akrit-agrawal/")

# time.sleep(15)

# # Take a screenshot and save it as 'screenshot.png'
# driver.save_screenshot("screenshot.png")

# # Quit the WebDriver session
# driver.quit()


# #Open AI

def analyze_linkedin_page(image_path):

  dotenv_path = Path('.env')
  load_dotenv(dotenv_path=dotenv_path)

  client = OpenAI()

  def encode_image(image_path):
    with open(image_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')

  base64_image = encode_image(image_path)

  response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "system", "content": "you are a lindkedIn Page analyzer bot and will give a accurate description of the person on the LinkedIn page"},
      {"role": "user", "content": [
        {"type": "text", "text": "describe the person on this LinkedIn page in a few sentences in detail"},
        {"type": "image_url", "image_url": {
          "url": f"data:image/png;base64,{base64_image}"}
        }
      ]}
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  return response.choices[0].message.content

# Example usage
result = analyze_linkedin_page('screenshot.png')
print(result)
