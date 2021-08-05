def BinarySearch(arr):
    lb, ub, index, isfound = 0, len(arr), 0, False
    item = int(input("No. you want to find: "))
    while not isfound and lb <= ub:
        index = ub + lb
        index //= 2
        if arr[index] == item:
            isfound = True
        elif arr[index] > item:
            ub = index - 1
        else:
            lb = index + 1
    if isfound:
        print(f"Item found at {index}")
    else:
        print("Error 404")
