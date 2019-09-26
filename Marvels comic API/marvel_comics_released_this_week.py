import marvelous
import pyttsx3
from os import system,name 
from time import sleep 
public_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
private_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

m = marvelous.api(public_key, private_key)

engine = pyttsx3.init();
system('cls')
print("enter the type of comic you are looking")
engine.say("enter the type of comic you are looking");
engine.runAndWait();

print("\n\ncomic\nmagazine\ntrade paperback\nhardcover\ndigest\ngraphic novel\ndigital comic\ninfinite comic\n\n")
a=input("enter your choice:-")
print("Enter which duration comic you want")
engine.say("Enter which duration comic you want");
engine.runAndWait();
print("\n\nthisWeek\nnextWeek\nlastWeek\nthisMonth")
b=input("enter your choice:-")
pulls = sorted(m.comics({
    'format': "comic",
    'formatType': a,
    'noVariants': True,
    'dateDescriptor': b,
    'limit': 100}),
    key=lambda comic: comic.title)
print('\033c')
c=[]
system('cls')



print("The list of comic are with format:-\n\n\n")

engine.say("The list of comic are with format:-");
engine.runAndWait();


for comic in pulls:
     print('{} (series #{})  (Format {}'.format(comic.title, comic.series.id,comic.format))
     c.append([[comic.title],[comic.series.id],[comic.format]])

sleep(8)
system('cls')


print("The simple list is:-\n\n\n\n")


engine.say("The simple list is");
engine.runAndWait();


for x in c:
	print(x[0])
