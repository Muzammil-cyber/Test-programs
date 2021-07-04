# Take class marks and name as input, output class avg and highest marks and lowest marks.
def enter():
    limit = int(input("How many students are there: "))
    print(limit)
    totmarks = int(input("Total marks of the test: "))
    names = [""]*limit
    marks = [0]*limit
    for x in range(limit):
        names[x] = input("Enter name of student: ")
        names[x] = names[x].strip()
        a = names[x]
        names[x] = a[0].upper() + a[1:]
        txt = "Enter marks of {}, from 0 to {}"
        marks[x] = int(input(txt.format(names[x], totmarks)))
        while marks[x] > totmarks or marks[x] < 0:
            marks[x] = int(input("Please," + txt.format(names[x], totmarks)))
    loop(marks, totmarks, limit)
    print(names, marks)


def loop(marks, totmarks, classsize):
    total = 0
    highest = -1
    lowest = totmarks - 1
    for x in range(classsize):
        totmarks += 1
        highest = high(marks[x], highest)
        lowest = low(marks[x], lowest)
        total += marks[x]
    print("Highest marks are, ", highest, "\nLowest marks are, ", lowest,"\nAverage marks are, ", round(total/classsize))


def high(mark, highmark):
    if mark > highmark:
        highmark = mark
    return highmark


def low(mark, lowmark):
    if mark < lowmark:
        lowmark = mark
    return lowmark


enter()
