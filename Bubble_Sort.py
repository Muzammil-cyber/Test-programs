#creates an array of letters' randomly organized
import random
arr = [""]*26
for x in range(26):
    arr[x] = chr(65+x)
random.shuffle(arr)
print(arr)

# Bubble Sort
for y in range(25,0,-1):
    isSorted = True
    for i in range(y):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            isSorted= False
    if isSorted == True: break
print(arr)

# Check whether sorted or not 1.0
flag = False
i = 1
while i < len(arr):
    if (arr[i] < arr[i - 1]):
        flag = True
    i += 1
if (not flag):
    print("Yes, List is sorted.")
else:
    print("No, List is not sorted.")
# Check whether sorted or not 2.0
darr = arr.copy()
darr.sort()
if darr==arr :
    print("It is sorted")
else:
    print("Not sorted")
