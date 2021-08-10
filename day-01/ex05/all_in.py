import sys

def get_capital_from_state(capital):
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
    
    result = get_state(capital)
    result = get_capital(result)
    return result

def get_state_from_capital(state):
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
    result = get_capital(state)
    result = get_state(result)
    return result

def is_empty(s):
    i = 0
    while i < len(s):
        if s[i] != ' ':
            return False
        i += 1
    return True

def edit_str(s):
    l = s.split(',')
    i = 0
    while i < len(l):
        l[i] = l[i].strip()
        i += 1
    return l

def capitalize_first_chars(s):
    if (len(s) == 0):
        return s
    tmp = s[0]
    tmp = tmp.capitalize()
    res = ""
    res += tmp
    i = 1
    while i < len(s):
        if (i > 1 and s[i - 1] == ' '):
            tmp = s[i]
            tmp = tmp.capitalize()
            res += tmp[0]
        else:
            tmp = s[i]
            tmp = tmp.lower()
            res += tmp[0]
        i += 1
    return res

def get_result(l, old_l):
    i = 0
    while i < len(l):
        res_1 = get_capital_from_state(l[i])
        res_2 = get_state_from_capital(l[i])
        if (res_1):
            print(f'{res_1} is the capital of {l[i]}')
        elif (res_2):
            print(f'{l[i]} is the capital of {res_2}')
        elif (is_empty(l[i]) == False):
            print(f'{old_l[i]} is neither a capital city nor a state')
        i += 1


def main():
    if (len(sys.argv) != 2):
        return None
    old_l = edit_str(sys.argv[1])
    new_l = list(old_l)
    
    i = 0
    while i < len(new_l):
        new_l[i] = capitalize_first_chars(new_l[i])
        i += 1
    get_result(new_l, old_l)

if __name__ == '__main__':
    main()