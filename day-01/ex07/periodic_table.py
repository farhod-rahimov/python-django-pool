import sys

def create_dict_from_file(file):
    i = 0
    while i < len(file):
        file[i] = file[i].split(' = ')
        file[i][1] = file[i][1].split(', ')
        i += 1

    i = 0
    while i < len(file):
        k = 0
        while k < len(file[i][1]):
            file[i][1][k] = file[i][1][k].split(':')
            new_dict = {file[i][1][k][0] : file[i][1][k][1]}
            file[i][1][k] = new_dict
            k += 1
        i += 1

    i = 0
    while i < len(file):
        k = 1
        while k < len(file[i][1]):
            file[i][1][0].update(file[i][1][k].copy())
            k += 1
        while len(file[i][1]) > 1:
            file[i][1].pop(len(file[i][1]) - 1)
        i += 1
    return file

def read_file(file_name):
    file = list()
    with open(file_name, 'r') as f:
        s = f.readline()
        while len(s):
            s = s.replace('\n', '')
            file.append(s)
            s = f.readline()
    return file

# ------------------------------------------------------------------------------------- #

def start_html(f):
    text = "<!DOCTYPE html>\n"
    text += "<html lang=\"en\">\n"
    text += "  <head>\n"
    text += "      <meta charset=\"UTF-8\">\n"
    text += "          <title>Periodic table</title>\n"
    text += "  </head>\n"
    text += "  <body>\n"
    f.write(text)

    return None

def create_table(f):
    text = "        <h1>Periodic table</h1>\n"
    f.write(text)
    
    return

def end_html(f):
    text = "  </body>\n"
    text = "</html>\n"
    f.write(text)
    
    return None

def create_html_file(html_name, edited_file):
    with open(html_name, 'w') as f:
        start_html(f)
        create_table(f)
        end_html(f)


def main():
    file = read_file("periodic_table.txt")
    edited_file = create_dict_from_file(file)
    create_html_file("periodic_table.html", edited_file)


if __name__ == '__main__':
    main()



# print(my_dict[0])                           # first line
# print(my_dict[0][0])                        # name of element
# print(my_dict[0][1][0])                      # dict
# print(my_dict[0][1][0]['position'])         # position

# /Users/btammara/django/day-01/ex07