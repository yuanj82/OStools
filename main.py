from functions.ID_converter import ID_converter
from functions.Extract_protein import Extract_protein

def Start_Information():
    print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print("#                                                                                             #")
    print("# You can choose the following functions                                                      #")
    print("#                                                                                             #")
    print("# 1 : ID_converter                                                                            #")
    print("# 2 : Extract_protein                                                                         #")
    print("# q : Exit program                                                                            #")
    print("#                                                                                             #")
    print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")

def Function_selection():
    start = input("Please select a function:")
    while True:
        if start == '1':
            ID_converter()
            start = input("Please select a function:")
        elif start == '2':
            Extract_protein()
            start = input("Please select a function:")
        elif start == 'c':
            Start_Information()
            start = input("Please select a function:")
        elif start == 'q':
            exit(0)
        else:
            print("Invalid input. Please try again.")


while True:
    Start_Information()
    Function_selection()
