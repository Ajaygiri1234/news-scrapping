from django.shortcuts import render
# Create your views here.
def index(request):
    value=allhref()
    context={
        'value':value
    }
    for i in value:
        print(i)
    return render(request,'crawl/home.html',context)

from urllib import request
import requests
from bs4 import BeautifulSoup

def allhref():
    array = []
    link = ''
    heading = ''
    author_link = ''
    author_name = ''
    img = ''
    description = ''

    url = 'https://kathmandupost.com/'
    sourcecode = requests.get(url)
    plaintext = sourcecode.text
    soup = BeautifulSoup(plaintext, 'html.parser')  #

    # above two line can be eliminated by one line
    # not needed plaintext = sourcecode.text
    # soup = BeautifulSoup(sourcecode.txt, 'html.parser')
    articles = soup.find_all('article', class_='article-image')  # array
    print(articles)
    for article in articles:
        print("withclass")

        def twoloopscrap(tag, clas=None):  # wlocal function
            inside_array = ['', '']
            for i in article.find_all(tag, class_=clas):

                print(i.find_all('a'))
                for j in i.find_all('a'):  # of for j in i
                    print(j.get('href'))
                    inside_array[0] = j.get('href')
                    for p in j:
                        print(p)
                        inside_array[1] = p
            return inside_array

        print(1)
        linktodetail_heading_array = twoloopscrap('h3')
        link = str('https://kathmandupost.com') + linktodetail_heading_array[0]
        heading = linktodetail_heading_array[1]
        print(2)
        linktoauthor_authorname_array = twoloopscrap('span', 'article-author')
        author_link = linktoauthor_authorname_array[0]
        author_name = linktoauthor_authorname_array[1]

        print(3)
        for i in article.find_all('img'):
            print(i.get('data-src'))
            img = i.get('data-src')

        print(4)
        for description in article.find_all('p'):
            for i in description:
                print(i)
                description = i

        array.append({'link': link, 'heading': heading, 'author_link': author_link, 'author_name': author_name, 'img': img,'description': description})

    array.append({'heading':'❤','link':'❤', 'author_link': author_link, 'author_name': author_name, 'img': img,'description': description})
    array.append({'heading':'\u00f0\u009f\u0098\u0080','link':'\u00f0\u009f\u0098\u0080', 'author_link': author_link, 'author_name': author_name, 'img': img,'description': '\u00f0\u009f\u0098\u0080'})
    array.append({'heading':'😀😃😄😁😆😅😂🤣☺️😊','link':'😀😃😄😁😆😅😂🤣☺️😊', 'author_link': author_link, 'author_name': author_name, 'img': img,'description': description})
    array.append({'heading':'😀😃😄😁😆😅😂🤣☺😊','link':'😀😃😄😁😆😅😂🤣☺😊', 'author_link': author_link, 'author_name': author_name, 'img': img,'description': description})
    return array


