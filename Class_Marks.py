#It takes student name and marks and output Average, highest marks with student name and lowest marks
stdname = [""]*5
marks = [-1]*len(stdname)
highest = -1
lowest = 101
total = 0
highstd = ""
for x in range (len(stdname)):
    stdname = input("Enter Name: ")
    stdname = stdname.strip()
    txt = "Enter marks of {} : "
    while marks[x] < 0 or marks[x] > 100:
        marks[x] = int(input(txt.format(stdname)))
    total += marks[x]
    if marks[x] > highest:
        highest = marks[x]
        highstd = stdname
    if marks[x] < lowest:
        lowest = marks[x]
print(highstd, " got the highest marks, ", highest, "\nAverage = ", total/len(stdname), "Lowest = ", lowest)
