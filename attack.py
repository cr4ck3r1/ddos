import uuid
import requests
import time
import os

c = input("nawt chia? ")
    
e = str(uuid.uuid5(uuid.NAMESPACE_DNS, c))
print("")
print(e)
g = requests.get("https://pastebin.com/2WuEPjdc")

if e in g.text:
    print("active")
    time.sleep(2)
    from lazyddos import hack
    hack()
    
else:
    print("id'akat active nia ")
    print("")
    print("nama bo instakam bnera")
    print("")
    print(" instagram: ara_software")