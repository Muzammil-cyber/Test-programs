fp, hp = 0, -1
mylist, mylistpointer = [""] * 10, [0] * 10
for x in range(9):
    mylistpointer[x] = x + 1
mylistpointer[9] = hp
print(mylistpointer)


def init(item):
    global fp, hp
    if fp == -1:
        print("List is full")
    else:
        mylist[fp] = item
        hp = fp
        fp = mylistpointer[fp]


def find(item):
    pointer = 0
    while True:
        if mylist[pointer] == item:
            print("Item Found")
            break
        else:
            pointer = mylistpointer[pointer]
            if pointer == -1:
                print("ERROR 404")
                break
    
    # OR #
""" pointer = 0
    found = False
    while not found and pointer != -1:
        if mylist[pointer] == item:
            found = True
        else:
            pointer = mylistpointer[pointer]
    if found:
        print("Item Found")
    else:
        print("ERROR 404")
"""
