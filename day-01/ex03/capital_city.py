import sys

def get_state(key):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    try:
        val = states[key]
        return val
    except KeyError:
        return None

def get_capital(key):
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    try:
        val = capital_cities[key]
        return val
    except KeyError:
        return None

def main():
    if (len(sys.argv) != 2):
        return None
    key = get_state(sys.argv[1])
    value = get_capital(key)
    if value != None:
        print(value)

if __name__ == '__main__':
    main()
