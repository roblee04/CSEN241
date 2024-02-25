import os
import subprocess
import requests
from datetime import datetime
import time

def main():
    

    # res = os.popen("curl localhost:8080/function/figlet -d " + words).read()

    # res = subprocess.run(["curl", "localhost:8080/function/figlet", "-d", words])
    # print(res)

    # Problem 7
    #############################################################################
    # A

    words = "what is your name?\n"
    figlet_url = "http://10.62.0.5:8080/function/chatbot"

    start = time.time()
    res = requests.post(figlet_url, words)
    end = time.time()

    print(end - start)
    
    #############################################################################
    # B

    words = "what is your name?\n"
    figlet_url = "http://10.62.0.5:8080/function/chatbot"
    res = requests.post(figlet_url, words)

    start = time.time()
    res = requests.post(figlet_url, words)
    end = time.time()

    print(end - start)

    #############################################################################
    # C

    words = "what is your name?\n"
    figlet_url = "http://10.62.0.5:8080/function/chatbot"

    total_time = 0
    for i in range(10):
        start = time.time()
        res = requests.post(figlet_url, words)
        end = time.time()

        total_time += (end - start)

    print(total_time / 10)


    #############################################################################
    # D

    words = "say cucumber?\n"
    figlet_url = "http://10.62.0.5:8080/function/chatbot"
    
    start = time.time()
    res = requests.post(figlet_url, words)
    end = time.time()

    print(end - start)


    #############################################################################
    # E

    words = "say cucumber?\n"

    figlet_url = "http://10.62.0.5:8080/function/chatbot"

    res = requests.post(figlet_url, words)

    start = time.time()
    res = requests.post(figlet_url, words)
    end = time.time()

    print(end - start)

    #############################################################################
    # F

    words = "name?\n"
    figlet_words = "say cucumber?\n"

    figlet_url = "http://10.62.0.5:8080/function/chatbot"

    res = requests.post(figlet_url, words)

    start = time.time()
    res = requests.post(figlet_url, figlet_words)
    end = time.time()

    print(end - start)
    
    #############################################################################
    # G
    
    words = "what is your name?\n"
    figlet_url = "http://10.62.0.5:8080/function/chatbot"

    total_time = 0
    for i in range(10):
        start = time.time()
        res = requests.post(figlet_url, words)
        end = time.time()

        total_time += (end - start)

    print(total_time / 10)


    #############################################################################

    # Problem 8
    # parallel





main()