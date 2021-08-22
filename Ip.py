import requests
import json


print("IP info....")

ip = input("Enter Your Ip Adress :")
url = "http://ip-api.com/json/" + ip

rp = requests.get(url)

data =json.loads(rp.content)

print(type(data))
print(data)
for x in data:
    print( x + "\t\t\t\t" + str(data[x]  +  "\n"))
