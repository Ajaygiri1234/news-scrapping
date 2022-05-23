from urllib import request
import requests
from bs4 import BeautifulSoup
import webbrowser


def spider():
    url='https://www.merriam-webster.com/dictionary/some'
    sourcecode=requests.get(url)
    plaintext=sourcecode.text
    soup=BeautifulSoup(plaintext,'html.parser')#

                 #above two line can be eliminated by one line
                        # not needed plaintext = sourcecode.text
                   #soup = BeautifulSoup(sourcecode.txt, 'html.parser')
    allhtml=soup.find_all('a')
    for link in allhtml: # for one loop link=output <a class="sth " href=sth></a>

        print(link)
        input("enter 1")
        href=link.get('href')#type = string
        print(href)
        input("enter 2 ")
        # add http//..... if the obtain href in not in correct format
        for item in href:
            if item=="/":
                href=str('https://www.merriam-webster.com')+href
            break
        print(href)
#spider()


def spider2():
    url='https://www.merriam-webster.com/dictionary/some'
    sourcecode=requests.get(url)
    plaintext=sourcecode.text
    soup=BeautifulSoup(plaintext,'html.parser')#

                 #above two line can be eliminated by one line
                        # not needed plaintext = sourcecode.text
                   #soup = BeautifulSoup(sourcecode.txt, 'html.parser')
    withclassa= soup.find_all(class_='footer-menu browse-dictionary') #array
    print(withclassa)

    for item in withclassa:
        print("withclass")
        print(item.find_all('a'))
        for i in item.find_all('a'):
            print(i)

            for j in i:
                print(j)



    input("enter")
    for itemss in withclassa:
        items=itemss.find_all('a')
        for item in items:
            href=item.get('href')
            for content in item:
                print(content)
            href = str('https://www.merriam-webster.com') + href
            print(href)
#spider2()


def runbrowser():
    import webbrowser
    #chrome="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
    website="https://www.youtube.com/watch?v=pLHejmLB16o&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_&index=27"
    webbrowser.open_new_tab(website)
    print("success")
#runbrowser()


def googlesearch():
    url='https://www.google.com/search?q=apple'
    print(1)
    sourcecode=requests.get(url)
    plaintext=sourcecode.text
    file=open('google.html',"w")
    file.write(plaintext)
    file.close()
    print(plaintext)
#googlesearch()


def spider21():
    array=[]
    link = ''
    heading =''
    author_link = ''
    author_name = ''
    img=''
    discription=''

    url='https://kathmandupost.com/'
    sourcecode=requests.get(url)
    plaintext=sourcecode.text
    soup=BeautifulSoup(plaintext,'html.parser')#

                 #above two line can be eliminated by one line
                        # not needed plaintext = sourcecode.text
                   #soup = BeautifulSoup(sourcecode.txt, 'html.parser')
    articles= soup.find_all('article', class_='article-image') #array
    print(articles)
    for article in articles:
        print("withclass")
        def twoloopscrap(tag,clas=None):#wlocal function
            inside_array = ['','']
            for i in article.find_all(tag,class_=clas):

                print(i.find_all('a'))
                for j in i.find_all('a'):  # of for j in i
                    print(j.get('href'))
                    inside_array[0]=j.get('href')
                    for p in j:
                        print(p)
                        inside_array[1]=p
            return inside_array
        print(1)
        linktodetail_heading_array=twoloopscrap('h3')
        link = str('https://kathmandupost.com/') + linktodetail_heading_array[0]
        heading=linktodetail_heading_array[1]
        print(2)
        linktoauthor_authorname_array=twoloopscrap('span','article-author')
        author_link=linktoauthor_authorname_array[0]
        author_name=linktoauthor_authorname_array[1]


        print(3)
        for i in article.find_all('img'):
            print(i.get('data-src'))
            img=i.get('data-src')



        print(4)
        for discription in article.find_all('p'):
            for i in discription:
                print(i)
                discription=i


        array.append({'link':link,'heading':heading,'author_link':author_link,'author_name':author_name,'img':img,'discription':discription})






spider21()

