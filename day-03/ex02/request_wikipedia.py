
import sys
import json

import requests
from dewiki import parser

# def search(search_str, url):
#     params = {

#     }

def main():
    url = "https://en.wikipedia.org/w/api.php"

    if len(sys.argv) != 2:
        print("Error. Wrong number of arguments. Expected 1", file=sys.stderr)
        sys.exit(1)
    
    search_page = sys.argv[1]
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": search_page
    }

    response = requests.get(url, params)

    if (response.status_code == 404):
        print(f"Error. Page for {sys.argv[1]} in en.wikipedia.org does not exist", file=sys.stderr)
        sys.exit(1)
    elif (response.status_code != 200):
        print(f"Error.", file=sys.stderr)
        sys.exit(1)

    response = response.json()
    print(response['query']['search'][0]['title'])
    
    # ------------------------------------------------------ #
    
    # params = {
    #     "action": "query",
    #     "prop": "revisions",
    #     "titles": response['query']['search'][0]['title'],
    #     # "rvslots": "*",
    #     "rvprop": "content",
    #     "format": "json"
    # }

    params = {
        "action": "parse",
        "page": response['query']['search'][0]['title'],
        "prop": "wikitext",
        "format": "json"
    }
    
    response = requests.get(url, params)

    if (response.status_code == 404):
        print(f"Error. Page for {sys.argv[1]} in en.wikipedia.org does not exist", file=sys.stderr)
        sys.exit(1)
    elif (response.status_code != 200):
        print(f"Error.", file=sys.stderr)
        sys.exit(1)

    response = response.json()
    # print(response['parse']['wikitext']['*'])

    print(parser.Parser().parse_string(response['parse']['wikitext']['*']))

    # json.dump(response.text, sys.stdout)

if __name__ == '__main__':
    main()