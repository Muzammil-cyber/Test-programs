#Updated
#It takes student name and marks and how many students are there, then it output's Average, highest marks with student name and lowest marks
limit = int(input("How many students in class: "))
stdname = [""]*limit
marks = [-1]*len(stdname)
highest = -1
lowest = 101
total = 0
highstd = ""
for x in range(limit):
    stdname[x] = input("Enter Name: ")
    stdname[x] = stdname[x].strip()
    a = stdname[x]
    stdname[x] = a[0].upper()+a[1:]
    txt = "Enter marks of {} : "
    while marks[x] < 0 or marks[x] > 100:
        marks[x] = int(input(txt.format(stdname[x])))
    total += marks[x]
    if marks[x] > highest:
        highest = marks[x]
        highstd = stdname[x]
    if marks[x] < lowest:
        lowest = marks[x]
print(highstd, " got the highest marks, ", highest, "\nAverage = ", total/limit, "Lowest = ", lowest)
