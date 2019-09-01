from time import *
from os import system
import pyfiglet

print("\a")
for x in range(30):
	l=asctime()
	k=pyfiglet.figlet_format(l, font = "bulbhead" )
	print(k)
	sleep(1)
	system('cls')
print("\a")