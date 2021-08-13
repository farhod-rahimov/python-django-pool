from local_lib import path as lib

def main():
    parent_dir = lib.os.getcwd()
    new_dir = "new_folder"
    
    new_dir_path = lib.os.path.join(parent_dir, new_dir)
    new_file_path = lib.os.path.join(new_dir_path, 'new_file.txt')

    msg = "This is the output of day-03 ex-01"
    
    try:
        lib.os.mkdir(new_dir_path)
    except Exception:
        pass

    try:
        with open (new_file_path, 'w') as f:
            f.write(msg)
    except Exception:
        print(f'Cannot open \'{new_file_path}\' for writing', file=lib.sys.stderr)
    
    try:
        with open (new_file_path, 'r') as f:
            print(f.read())
    except Exception:
        print(f'Cannot open \'{new_file_path}\' for reading', file=lib.sys.stderr)

    return None

if __name__ == '__main__':
    main()
