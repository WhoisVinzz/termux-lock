import os
import requests
#INSERT SERVER KEY HERE
#CREATE ON https://api.vinz.my.id/termux-lock
server_key = "Default"
#END OF SERVER KEY
#UDAH GAUSAH EDIT" NTR ERROR
os.system("clear")
print("Loading...")
URL = f"https://api.vinz.my.id/termux-lock/{server_key}.json"
r = requests.get(url = URL) 
data = r.json() 
key = data['key']
if key == "":
  print("Server Key Not Found !")
else:
  command = data['command']
  name = data['name']
  os.system("clear")
  lock = "true"
  os.system(f"figlet Hi, {name}")
  print("Termux Login !\n\n")
  while lock == "true":
     password = input("Input PIN :")
     if password == key:
       lock = "false"
     os.system("clear")
     os.system(f"figlet Hi, {name}")
     print("Termux Login !\n\n")
     print("Incorrect Password, Try Again...")
  os.system("clear")
  os.system(f"figlet Hi, {name}")
  os.system("echo Welcome To Termux ! && echo")
  os.system(f"{command}")
    
