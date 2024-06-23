import requests
from time import sleep

with open('./user_id', 'r') as file:
    user_id = file.read()

if user_id == "":
    print("Please add the your telegram user id in the file 'user_id', check the README to see how to retrieve it.")
    exit(1)

url = "https://miner-webapp-fz9k.vercel.app/api/claim?id=" + user_id

try:
    while True:
        req = requests.post(url)
        print(req.json())
        sleep(60*60) # every hour
except KeyboardInterrupt:
    print("exit.")