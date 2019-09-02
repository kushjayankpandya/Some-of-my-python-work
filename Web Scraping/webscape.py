import requests
from bs4 import BeautifulSoup





href1="http://quotes.toscrape.com/"
href2=''

quotes=[]
n=0
print('-------------------------------------------------------------------------')
print('\t\t page1')
while(1):
    n+=1
    bod=requests.get(href1+href2)
    main=BeautifulSoup(bod.text,"html.parser")
    body=main.find('body')
    
    quote=body.find_all(class_='quote')
    
    for x in quote:
        text=x.find(class_='text')
        author=x.find(class_='author')
        
        parent=author.parent
        href3=parent.find('a')['href']
        bod=requests.get(href1+href3)
        main2=BeautifulSoup(bod.text,"html.parser")
        A_B_D=main2.find(class_='author-born-date')
        
        if text!=None and author!=None:
            print(text.get_text())
            print("\n")
            print(author.get_text()+'\n'+A_B_D.parent.get_text())
            print('\n\n')       
    nav=body.find('nav')
    li=nav.find(class_='next')
    if li==None:
        break
    href2=li.find('a')['href']
    print('-------------------------------------------------------------------------------------------')
    print('\n\n\n\n\t\t'+href2+'\n\n\n\n')
    

        

