print("Welcome to Calculator \n Made by Muzammil")
ans = float(input("First Number: "))
n2 = float(input("Second Number: "))
while n2 != 0:
    op = input("Input operator: ")
    while not op == "+" and op == "-" and op == "*" and op == "x" and op == "/":
        op = input("Please enter the correct operator(+,-,*,/): ")
    if op == "+":
        ans += n2
    elif op == "-":
         ans -= n2
    elif op == "/":
        ans = ans/n2
    else:
        ans *= n2
    print(ans)
    n2 = float(input("Another Number: "))
print("The End!!")
