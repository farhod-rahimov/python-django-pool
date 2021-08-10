import sys

def get_state(value):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    try:
        for k, v in states.items():
            if (v == value):
                return k
        return None
    except KeyError:
        return None

def get_capital(value):
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    try:
        for k, v in capital_cities.items():
            if (v == value):
                return k
        return None
    except KeyError:
        return None

def main():
    if (len(sys.argv) != 2):
        return None
    value = get_capital(sys.argv[1])
    key = get_state(value)

    if key != None:
        print(key)

if __name__ == '__main__':
    main()