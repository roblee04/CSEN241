import threading
import requests
import time
import subprocess

num_threads = 10
thread_num_req = 1

def main():
    
    while(1):
        total_threads = 0
        start = time.time()
        threads = []

        for i in range(num_threads):
            t1 = threading.Thread(target=function_call, args=())
            threads.append(t1)
            total_threads += 1
            t1.start()
        
        for t in threads:
            t.join()

        time_slice = time.time() - start
        print((total_threads * thread_num_req) / time_slice)

 
def function_call():
    words = "what is your name?\n"
    figlet_url = "http://localhost:8080/async-function/chatbot"
    # header = "X-Callback-Url: http://localhost:8888"
    for i in range(thread_num_req):
        res = requests.post(figlet_url, words)
        # print(res.text)
    return

main()