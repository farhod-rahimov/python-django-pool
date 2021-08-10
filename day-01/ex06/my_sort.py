def sort_func():
    d = {
        'Hendrix' : '1942',
        'Allman' : '1946',
        'King' : '1925',
        'Clapton' : '1945',
        'Johnson' : '1911',
        'Berry' : '1926',
        'Vaughan' : '1954',
        'Cooder' : '1947',
        'Page' : '1944',
        'Richards' : '1943',
        'Hammett' : '1962',
        'Cobain' : '1967',
        'Garcia' : '1942',
        'Beck' : '1944',
        'Santana' : '1947',
        'Ramone' : '1948',
        'White' : '1975',
        'Frusciante': '1970',
        'Thompson' : '1949',
        'Burton' : '1939',
        }
    
    list_tuples = list()
    list_keys = list(d.keys())
    tmp_list = list()

    i = 0
    while i < len(list_keys):
        tmp_list.append(d[list_keys[i]])
        tmp_list.append(list_keys[i])
        list_tuples.append(tuple(list(tmp_list)))
        tmp_list.clear()
        i += 1

    list_tuples.sort()

    new_dict = {v : k for k, v in list_tuples}
    for k, v in new_dict.items():
        print(k)
        # print(k, ':', v)

if __name__ == '__main__':
	sort_func()