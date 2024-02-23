import os
import subprocess
import requests
from datetime import datetime

def main():
    words = "hello worlds"
    # res = os.popen("curl localhost:8080/function/figlet -d " + words).read()

    # res = subprocess.run(["curl", "localhost:8080/function/figlet", "-d", words])
    # print(res)

    now = datetime.now()
    print(str(now) + "hry")
    figlet_url = "http://10.62.0.5:8080/function/figlet"
    res = requests.post(figlet_url, words)
    print(res.text)
    return res.text
main()