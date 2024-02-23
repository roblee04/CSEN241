
# faas-cli build -f ./chatbot.yml 
# faas-cli push -f ./chatbot.yml 

import os
import subprocess
import requests
import urllib
from datetime import datetime

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    chatbot_name = "Bob the Builder"

    greeting = ["name?\n", "what is your name?\n", "sup dog\n"]
    time_query = ["time?\n", "what is the time?\n", "clock\n"]
    big_word = ["say"]

    user_input = urllib.unquote(urllib.unquote(req).decode('utf8'))

    if user_input in greeting:
        if user_input == "name?\n":
            return "my name is " + chatbot_name
        elif user_input == "what is your name?\n":
            return chatbot_name
        else:
            return "whats up big dog! YA boy " + chatbot_name + " is killin it"

    elif user_input in time_query:
        now = datetime.now()
        date = str(datetime.date(now))
        time = str(datetime.time(now))

        if user_input == "time?\n":
            return "Today is " + date + " and it is " + time
        elif user_input == "what is the time?\n":
            return "The time is " + time + " and today is " + date
        else:
            return "Current Time = " + str(now)

    else:
        if len(user_input.split()) == 1:
            return user_input

        words = user_input
        say, words = user_input.split(" ", 1)
        words = str(words)
    
        # res = os.popen("curl localhost:8080/function/figlet -d " + words).read()
        # res2 = subprocess.run(["curl", "localhost:8080/function/figlet", "-d", words])

        figlet_url = "http://10.62.0.5:8080/function/figlet"
        res = requests.post(figlet_url, words)
        
        return res.text
