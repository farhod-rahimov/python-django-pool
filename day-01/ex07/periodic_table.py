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
    text += "   <head>\n"
    text += "      <meta charset=\"UTF-8\">\n"
    text += "          <title>Periodic table</title>\n"
    text += "   </head>\n"
    text += "   <body>\n"
    text += "       <table>\n"
    text += "           <tr>\n"
    text += "               <td style=\"border: 1px solid black; padding:10px\">\n"
    
    f.write(text)
    return None

def add_element_in_table(f,  data):
    # text = "        <h1>Periodic table</h1>\n"
    text = "                    <h4>" + data[0] + "/<h4>\n"
    text += "                       <ul>\n"
    text += "                           <li>No " + data[1][0]['number'].strip() + "</li>\n"
    text += "                           <li>" + data[1][0]['small'].strip() + "</li>\n"
    text += "                           <li>" + data[1][0]['molar'].strip() + "</li>\n"
    text += "                           <li>" + data[1][0]['electron'].strip() + "</li>\n"
    text += "                       </ul>\n"

    f.write(text)
    return None

def add_empty_element_in_table(f):
    text = "                    <h4> Empty" + "/<h4>\n"
    text += "                       <ul>\n"
    text += "                           <li>" + "</li>\n"
    text += "                           <li>" + "</li>\n"
    text += "                           <li>" + "</li>\n"
    text += "                           <li>" + "</li>\n"
    text += "                       </ul>\n"
    
    f.write(text)
    return None

def end_html(f):
    text = "               </td>\n"
    text += "           </tr>\n"
    text += "        </table>\n"
    text += "    </body>\n"
    text += "</html>\n"
    
    f.write(text)
    return None

def get_element_from_number(pos, edited_file):
    i = 0
    while i < len(edited_file):
        p = edited_file[i][1][0]['number']
        p = p.strip()
        if (pos == int(p)):
            return edited_file[i]
        i += 1
    return None


def create_html_file(html_name, edited_file):
    with open(html_name, 'w') as f:
        start_html(f)
        number = 1
        last_position = 0
        while number <= 118:
            element = get_element_from_number(number, edited_file)
            if (element != None):
                while last_position < int(element[1][0]['position'].strip()):
                    add_empty_element_in_table(f)
                    last_position += 1
                add_element_in_table(f, element)
                last_position = int(element[1][0]['position'].strip())
            # else:
            #     add_empty_element_in_table(f)
            number += 1
        end_html(f)
    return None

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