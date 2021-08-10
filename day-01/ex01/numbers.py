def split_by_comma(str):
    new_str = str.replace(',', '\n', str.count(','))
    return new_str

def work_with_file(name):
    with open(name, 'r') as f:
        str = f.read()
        new_str = split_by_comma(str)
        print(new_str, end='')

if __name__ == '__main__':
    work_with_file("numbers.txt")