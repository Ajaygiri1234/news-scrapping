from urllib import request
import requests
from bs4 import BeautifulSoup
import webbrowser

crawled_links=[]
previous=0

def spider2(url):

    sourcecode=requests.get(url)
    plaintext=sourcecode.text
    soup=BeautifulSoup(plaintext,'html.parser')#

                 #above two line can be eliminated by one line
                        # not needed plaintext = sourcecode.text
                   #soup = BeautifulSoup(sourcecode.txt, 'html.parser')
    links= soup.find_all('a') #array
    print(links)

    for link in links:
        try:

            href = link.get('href')

            try:
                sourcecode = requests.get(href)
                continue
            except:
                href = 'https://kathmandupost.com' + href
                if href.find('2020')==-1:
                    pass
                else:
                    print(2020)
                    print(href)
                    print(2020)


            if (href in crawled_links):
               # print("crawled")
                #print(href)
                continue
            else:
                crawled_links.append(href)
               # print(href)
                spider2(href)
        except:
            #print(1)
            continue


spider2('https://kathmandupost.com')
