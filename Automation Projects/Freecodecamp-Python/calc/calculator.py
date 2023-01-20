num1 = float(input("Enter the first number: "))
op = input("Enter the operation you want to do on the two numbers: ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Operation currently handled")
