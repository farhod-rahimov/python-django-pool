import sys

def main():
    with open("periodic_table.txt", 'r') as f:
        file = list()
        s = f.readline()
        while len(s):
            s = s.replace('\n', '')
            file.append(s)
            s = f.readline()
        
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

        # print(file)
        print(file[0])
        print(file[0][1][0]['position'])
        print(file[0][1][0]['number'])


if __name__ == '__main__':
    main()


# /Users/btammara/django/day-01/ex07