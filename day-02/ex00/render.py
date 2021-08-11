import sys
import os
import re

import settings as g_vars

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

def replace_vars(file_to_edit):
    file_to_edit = re.sub("{title}", str(g_vars.title), file_to_edit)
    file_to_edit = re.sub("{name}", str(g_vars.name), file_to_edit)
    file_to_edit = re.sub("{surname}", str(g_vars.surname), file_to_edit)
    file_to_edit = re.sub("{age}", str(g_vars.age), file_to_edit)
    file_to_edit = re.sub("{profession}", str(g_vars.profession), file_to_edit)

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

    edited_file = replace_vars(file_to_edit)
    create_new_html_file(edited_file)

main()