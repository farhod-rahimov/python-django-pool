import sys
import os
import re

# import settings as g_vars

def check_errors():
    if (len(sys.argv) != 2):
        print("Error. Wrong number of arguments", file=sys.stderr)
        sys.exit(1)
    file_name = sys.argv[1]
# ------------------------------------------------------------------ #

    l = file_name.split('.')
    
    if len(l) < 2:
        print(f'Error. File \'{file_name}\' has bad extension', file=sys.stderr)
        sys.exit(1)
    
    if l[len(l) - 1] != "template":
        print(f'Error. File \'{file_name}\' has bad extension', file=sys.stderr)
        sys.exit(1)

# ------------------------------------------------------------------ #
    
    try:
        fd = os.open(sys.argv[1], os.O_RDONLY)
    except Exception:
        print(f'Error. File \'{sys.argv[1]}\' does not exist', file=sys.stderr)
        sys.exit(1)

    try:
        fd = os.open("settings.py", os.O_RDONLY)
    except Exception:
        print(f'Error. File \'settings.py\' does not exist', file=sys.stderr)
        sys.exit(1)

    os.close(fd)

    return None

def replace_vars(g_vars, file_to_edit):
    tmp = ""

    i = 0
    while i < len(g_vars):
        tmp = "{"
        tmp += g_vars[i][0]
        tmp += "}"
        file_to_edit = re.sub(tmp, g_vars[i][1], file_to_edit)
        i += 1

    return file_to_edit

def create_new_html_file(text):
    i = 0
    new_file_name = ""
    while i < sys.argv[1].rfind('.'):
        new_file_name += sys.argv[1][i]
        i += 1
    new_file_name += ".html"

    with open(new_file_name, 'w') as f:
        f.write(text)

def main():
    check_errors()

    with open(sys.argv[1], 'r') as f:
        file_to_edit = f.read()

    with open("settings.py", 'r') as f:
        g_vars = f.read()
    
    g_vars = g_vars.split('\n')

    i = 0
    while i < len(g_vars):
        g_vars[i] = g_vars[i].split(' = ')
        g_vars[i][1] = str(g_vars[i][1]).strip('\"')
        g_vars[i][1] = str(g_vars[i][1]).strip('\'')
        g_vars[i] = tuple(g_vars[i])
        i += 1
    
    edited_file = replace_vars(g_vars, file_to_edit)
    create_new_html_file(edited_file)

main()