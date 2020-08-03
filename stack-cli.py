import requests
import re
from bs4 import BeautifulSoup
import sys


# This Function, gets inputs from a user and returns the search link
def get_url_from_user():
    while True:
        try:
            if len(sys.argv)>1:
                q=' '.join(sys.argv[1:])
                break
            else:
                print('Error: Enter an Argument')
                exit()
        except IndexError:
            print('Error: Enter an Argument')
            exit()

    #q = input('Enter your Search: ')
    user_search = integrate_into_google_search(q)

    return 'https://www.google.com/search?safe=active&q=' + user_search

#This function splits the input of the user and joins it by '+'
def integrate_into_google_search(search):
    split_search=search.split()
    join_by_add='+'.join(split_search)

    return join_by_add

#This function checks if the page loads successfully and coverts the page into a text or HTML format
def return_html(url):
    page=requests.get(url)

    if page.status_code==200:
        print('Page loaded successfully')
    else:
        print('Error Loading page')
    page_text=page.text
    return page_text


def get_links(soup):
    link=[]
    for links in soup.find_all('a'):
        link.append(links.get('href'))
    return link

google_url=get_url_from_user()
print('The google url is: ',google_url)
soup=BeautifulSoup(return_html(google_url),'html.parser')

arr_link= get_links(soup)
new_arr_link=[]
for link in arr_link:
    if 'https://stackoverflow.com' in link:
        new_arr_link.append(link.split('url?q=')[1])


if len(new_arr_link)>0:
    print('-------------------------------------------------------Stack overflow links-----------------------------------------------')

    for stack_link in new_arr_link:
        print(stack_link)
else:
    print('NO STACK OVERFLOW LINKS FOUND')



