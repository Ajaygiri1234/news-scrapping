from urllib import request
import requests
from bs4 import BeautifulSoup

def spider(max_pages):

    print(1)
    count=0
    page=1
    while (page<= max_pages):
        print(2)
        url='https://kathmandupost.com/'
        print(1)
        sourcecode=requests.get(url)
        plaintext=sourcecode.text
        soup=BeautifulSoup(plaintext,'html.parser')#

                     #above two line can be eliminated by one line
                            # not needed plaintext = sourcecode.text
        print(soup)
        try:
        #soup = BeautifulSoup(sourcecode.txt, 'html.parser')
            for link in soup.find_all('a'):
                print(link)
                try:
                    for i in link:
                        print(i)
                except:
                    continue



                href=link.get('href')
                try:
                    for item in href:
                        if item=="/":
                            href=str('https://kathmandupost.com')+href
                            count= count+1

                        break
                except:
                    continue
                print(href)
                input("jh")
        except:
            pass
        print(count)
        page=page+1

spider(1)
