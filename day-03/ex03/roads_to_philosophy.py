import sys
import requests
from bs4 import BeautifulSoup

def get_href(soap, prefix):
    for p in soap.find_all('p'):
        for link in p.find_all('a'):
            href = link.get('href')
            if href == None:
                continue
            i = 0
            for c in str(href):
                if i >= len(prefix) or c != prefix[i]:
                    break
                i += 1
            if i == len(prefix) and href.find(':') < 0:
                return href
    
    return None

def check_inf_loop(all_titles, current_title):
    for title in all_titles:
        if title == current_title:
            return True
    return False

def main():
    main_url = "https://en.wikipedia.org"
    
    if len(sys.argv) != 2:
        print("Error. Wrong number of arguments", file=sys.stderr)
        sys.exit(1)

    number = 0

    prefix = "/wiki/"
    all_titles = list()

    url = main_url + "/wiki/" + sys.argv[1]
    while 21:
        number += 1
        response = requests.get(url)

        if response.status_code != 200:
            print (f'Server error {response.status_code} {response.reason}', file=sys.stderr)
            sys.exit(1)
        
        soap = BeautifulSoup(response.text, 'html.parser')
        if check_inf_loop(all_titles, soap.title.text) == True:
            print (' It leads to an infinite loop !')
            sys.exit(0)

        all_titles.append(soap.title.text)
        print (soap.title.text)

        if (soap.title.text == "Philosophy - Wikipedia"):
            print(f'{number} roads from {sys.argv[1]} to philosophy')
            sys.exit(0)

        url = get_href(soap, prefix)
        if url == None:
            print ('It leads to a dead end !')
            sys.exit(0)
        
        url = main_url + url
    return 0

if __name__ == '__main__':
    main()