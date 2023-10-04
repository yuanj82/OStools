import os

def ID_converter():
    gene= input(str("Please input id:"))

    current_path = os.path.abspath(__file__)
    root_path = os.path.dirname(current_path)
    IDfile = os.path.join(root_path, '../data', 'ID.txt')

    with open(IDfile, "r+") as file:
        ID_corresponding_list = file.readlines()

    for ID in ID_corresponding_list:
        if gene in ID:
            print('OS ID:{}'.format(ID.split('\t')[0]))
            print('LOC ID:{}'.format(ID.split('\t')[1]))
            break
        else:
            continue
    else:
        print("sorry, ID not found!")
        
    print("ID conversion completed!")
    print()