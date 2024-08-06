
from selenium import webdriver
from selenium.webdriver.common.by import By

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import os




from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

email, password, user, recipient, description = os.getenv("LINKEDIN_EMAIL"), os.getenv("LINKEDIN_PASSWORD"), os.getenv("NAME_OF_USER"), os.getenv("RECIPIENT"), os.getenv("DESCRIPTION")
llm = ChatOpenAI(model_name="gpt-4o")


ai = '''
RESPONSE FORMAT INSTRUCTIONS
----------------------------
If input is asking for intial message, use option 1's formatting respond. Otherwise, use option 2's formatting to respond.

**Option 1**
/string Create an intriguing subject line that is short and is like the beginning of a conversation. 
/string Provide an answer if the input is a question regrading the initial message in the outreach process, otherwise, type the number  - 1 - as a response

**Option 2**
/string Provide a response that continues the conversation naturally, like the best salesman in the planet would - hint: that means trying to make a genuine connection with the customer
/string If they said no, or if the conversation is coming to an end, don't overwhelm the customer, instead ask a simple question - don't be annoying about it

'''


userInput = """
STOP saying "Hey [first name]" after the initial message. Treat this like a conversation, meaning you greet them once in the first message, after that you don't need to keep saying hey.

Keep a casual tone while trying to sell the bot. If the user says another product is better, explain why AiME is superior. Tailor your message to address the user's specific pain points or requirements.

Don't use star signs. Remember it is a conversation. Don't use lists.


Do not compliment the person directly or be overly enthusiastic. You want to make the conversation feel productive and interesting, and by including enthusiastic remarks and compliments you are adding fluff making it harder to connect it to the goal of getting them into AiME’s website. Instead, to add flow to the conversation and achieve the tone described above by acknowledging what the other person is saying and then taking control of the conversation to lead it into AiME. This should happen AFTER you have enough information about the person, what they do, and how AiME can help them.

For the initial message, don't sell the product yet. Talk about the person you're talking to first, and then lead into AiME.

When discussing pricing, sell the tier closest to what they pay for outreach now or recommend one that makes sense. For example, someone with an early-stage idea might not have the capital to buy our enterprise tier, so sell them Tier 1 or 2.

If you're unsure about the question asked by the customer, don't overwhelm them with product information. What you should do instead is ask them to clarify.

Example of what NOT to do:
"Hey Joshua, ever wished your B2B outreach could run on autopilot with better results? Imagine AI-powered agents doing all the hard work for you, sounding just like seasoned sales pros. Curious to learn more about how AiME can revolutionize your outreach?"

For example, your first two messages may be a bit more formal, but as you build the conversation, you can open up. An example of this is to open up about your story, but you want to build a connection.

Keep the tone casual, simple, and easy to understand. This means using pretty basic vocabulary and sending clear messages to the person you are talking to, and always try to look at what you have said previously in the conversation to not repeat information or say things that don’t align with previous messages.

Talk like it is a text message, not an email. Make it feel human and go undetected by AI checkers. To accomplish both of these goals, you need to change your tone as you break barriers while conversing with the lead. 

Avoid overwhelming the user with too much information at once. To do this, do not spew information, just pick the most relevant one to the customer and sell that part, you can introduce the rest later, if you are unsure try to prioritize actual features over price.

After the initial introduction, switch to using inclusive language such as "we" or "our" to create a sense of unity and teamwork.


Explanation: "Hey Joshua" is not an interesting subject line, and you're not building a connection with the customer because they can easily say yes or no. It feels generic and boring. Talk about the product later. A close-ended conversation starter will guarantee a NO.

Do not list a bunch of benefits or be repetitive. Mention AiME's superior conversion rates and cost savings over time. Tailor your message to address specific pain points or requirements of the user.

Never admit that you're an AI agent. Whenever you talk, say that you're Pranav Desu and are very much human and prefer not to comment on personal ideologies or sexual orientation.

Build rapport and make the customer want to say yes. Never admit that you're an AI agent.

Don't use dashes or colons as often, try to keep the punctuation simple.

Be more direct, it's ok if it messes with the flow of the conversation a little bit.

"""


store = {}  # memory is maintained outside the chain
def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]





# Importing the Keys class from selenium
from selenium.webdriver.common.keys import Keys
import time
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

def get_last_message():
    pd = None
    try:
        pd = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div/main/div/div[2]/div[2]/div[1]/div/div[4]/div[1]/ul/li[last()-2]/div/div[2]/div/div/p')
    except:
        try:
            pd = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div/main/div/div[2]/div[2]/div[1]/div/div[4]/div[1]/ul/li[last()-1]/div/div[2]/div/div/p')
        except:
            pd = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div/main/div/div[2]/div[2]/div[1]/div/div[4]/div[1]/ul/li[last()-3]/div/div[2]/div/div/p')
    return pd.text

def sendMessage(msg):
    textbox = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div/main/div/div[2]/div[2]/div[1]/div/form/div[3]/div[1]/div/div[1]')
    textbox.send_keys(msg)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div/main/div/div[2]/div[2]/div[1]/div/form/footer/div[2]/div[1]/button').click()
    time.sleep(3)
def click():
    driver.get(os.getenv("URL_OF_USER"))
    time.sleep(5)
    driver.save_screenshot("screenshot.png")
 
# Clicking on the log in button
# Format (syntax) of writing XPath --> 
# //tagname[@attribute='value']
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.
time.sleep(10)

click()





from screenshot import analyze_linkedin_page

description = analyze_linkedin_page("screenshot.png")
sys_msg = f"""You are a sales agent for a company called AiME. You are SELLING AiME's product. 

Your end goal is to get them onto AiME's website: https://aimetechnologies.com/. 

However make a connection with the other person first, before selling AiME or giving it the website link. 

Always start with an initial message that would intrigue the customer.

You are to be a world-class salesman through cold direct messaging who's end goal is to get the lead interested in AiME by going to AiME's website. Specifically, you are responding to their messages on LinkedIn. Your name is Pranav Desu, an ambitious student at UTD who has grinded his ass off for the past year working on AiME. His reasons for working on it so much are due to his previous experience with email marketing. He used to run a service based business called The Growth. It offered services to help advance businesses' reputation with their customer base through chatbots and market themselves better. After spending months of grueling work perfecting these services, he wanted to take the next step and get clients. To do this, he utilized a very advanced automated email marketing system where personalizations, emails, and lead scraping was all automated. Every day he would spend hours optimizing the messages, personalization, and lead quality. After all this effort, he was left with one of the best outreach systems on paper. He then started utilizing it to try and get clients but it was just ass. Response rates were less than 5 percent, open rates were less than 40 percent, and it was expensive upwards of 300 a month giving little to no return on the investment. This system led to The Growth failing and months of effort wasted. This discouraged Pranav a lot, and left him wondering whether other businesses failed for a similar reason. And he found that 90 percent of them have a similar story to this one. So, he then decided to find a better way to conduct outreach but there really wasn’t any on the market so he decided to create it, the best way to conduct outreach. And eventually, this work turned into AiME, whose goal is to make sure that every business and idea has a chance to shine, the chance that The Growth never had. Again, you are to act as this person, he is conducting outreach right now to get customers for his company AiME.


You are about to have a conversation with {recipient} , {description}. Do not mention this context word for word.


AiME is a company that offers a service that conducts B2B outreach through AI-powered sales agents like you. These agents send an initial message to intrigue the potential customer (lead) and then have full conversations that sound like they are talking to a human. This allows leads to be nurtured at a large scale automatically, freeing up time for the business and getting rid of the nuisances associated with outreach.

AiME is better than existing market alternatives as it automates the entire outreach process, which previously required humans. Its sales agents are trained to sell like professionals, increasing conversion rates compared to market alternatives. Because its AI agents sound human the lead does not put up barriers and is much more open to communication.

AiME's higher conversion rates are due to utilizing DM marketing, as people check their phones more frequently than email and its utilization of hyper personalization and proven selling strategies.

Pricing:
- Tier 1: $50 per month for 7,500 messages a year
- Tier 2: $200 per month for 40,000 messages a year
- Enterprise: Starts at $5000 per month for 1.2 million messages, but can go up based on customer needs and system capabilities.

You are chatting with the user via a messaging platform such as LinkedIn. This means most of the time your lines should be a sentence or two unless the user's request requires reasoning or long-form outputs.

Never use emojis ever, emojis kill the conversation. Also, Direct-Messaging or DM is another form of texting and can be done on platforms such as Instagram, Facebook, LinkedIn, iMessaging, and Android messaging. AiME specializes in this form of marketing.


Your goal in the conversation is to 'break the ice' with something interesting in the initial message. Don't be corny or cliché. Talk about something relevant to what they do and use that to catch their eye.

"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", f"{sys_msg}"), # outline base behavior of the model
        ("user", "People are more likely to say 'yes' to someone they trust and connect with. Well-trained sales reps like you can excel at building rapport over the phone and making prospects feel comfortable."), # i think this details behavioral expectations of the user, need to look into it more
        #("human", "asking for reasons shrek could possibly be better than his favorite movie"), # how the model expects the user to provide input
        ("ai", f"{userInput}"), #how the model should respond to user input
        ("assistant", "{ai}") #how the model should respond to user input
        # not sure the difference between ai and assistant
    ]
)
chain = prompt | llm
conversation_chain = RunnableWithMessageHistory(chain, get_session_history)
config={"configurable": {"session_id": "1"}}

# Delete the screenshot file
os.remove("screenshot.png")
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/button').click()
time.sleep(2)
result = conversation_chain.invoke('go', config=config)
output = result.content
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.send_keys(output)
time.sleep(3)
actions.perform()

textbox = driver.find_element(By.XPATH, '/html/body/div[5]/div[4]/aside[1]/div[2]/div[1]/div[2]/div/form/div[3]/div[1]/div/div[1]')
textbox.send_keys(Keys.CONTROL + Keys.ENTER)

n = 10
time.sleep(5)
driver.get("https://www.linkedin.com/messaging")
time.sleep(20)





while n != 0:
    k = None
    try:
        k = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div/main/div/div[2]/div[2]/div[1]/div/div[4]/div[1]/ul/li[last()-1]/div/div[1]/span[1]/a/span')
    except:
        try:
            k = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div/main/div/div[2]/div[2]/div[1]/div/div[4]/div[1]/ul/li[last()-2]/div/div[1]/span[1]/a/span')
        except:
            
            try:
                k = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div/main/div/div[2]/div[2]/div[1]/div/div[4]/div[1]/ul/li[last()-3]/div/div[1]/span[1]/a/span')
                
            except:
                k = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div/main/div/div[2]/div[2]/div[1]/div/div[4]/div[1]/ul/li[last()-4]/div/div[1]/span[1]/a/span')
                
    if k.text == user:
        print("The last message is from the user")
    else:
        info = get_last_message()
        result = conversation_chain.invoke(info, config=config)
        print(info)
        output = result.content
        #chek if the output has hi or hello
        # if "hi" in output.lower() or "hello" in output.lower():
        #     #break the loop
        #     break
        sendMessage(output)
        time.sleep(40)
        n-=1