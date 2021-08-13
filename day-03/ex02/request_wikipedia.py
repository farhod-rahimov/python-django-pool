import requests
import json
from dewiki import parser
import sys


def check_error(response, search_str):
    if response.status_code != 200:
        print(f'Error. Page for {search_str} does not exist. Reason: {response.reason}', file=sys.stderr)


def search(search_str, url):
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": search_str
    }
    
    response = requests.get(url, params)
    check_error(response, search_str)
    response = response.json()

    if len(response['query']['search']) < 1:
        print(f'Error. Page for \'{search_str}\' does not exist')
        sys.exit(1)
    
    return(response['query']['search'][0]['title'])


def get_content(page, url):
    params = {
        "action": "parse",
        "page": page,
        "prop": "wikitext",
        "format": "json"
    }

    response = requests.get(url, params)
    check_error(response, page)
    
    return(response.json())


def save_text_in_file(text, file_name):
    file_name = file_name.replace(' ', '_')
    try:
        with open(file_name, 'w') as f:
            f.write(text)
    except Exception as err:
        print(err, file=sys.stderr)


def main():
    if len(sys.argv) != 2:
        print("Error. Wrong number of arguments. Expected 1", file=sys.stderr)
        sys.exit(1)
    
    url = "https://en.wikipedia.org/w/api.php"
    search_str = sys.argv[1]
    
    page_name = search(search_str, url)
    response = get_content(page_name, url)

    text = parser.Parser().parse_string(response['parse']['wikitext']['*'])

    save_text_in_file(text, page_name + '.wiki')

if __name__ == '__main__':
    main()