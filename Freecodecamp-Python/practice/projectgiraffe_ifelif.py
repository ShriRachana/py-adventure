#string,numeric and other data types can be compared with different comparison operators
num1 = input("Enter number 1 ")
num2 = input("Enter number 2 ")
num3 = input("Enter number 3 ")
def max_num(num1,num2,num3):
    if not num1.isdigit() or not num2.isdigit() or not num3.isdigit():
        return "Invalid number"
    else:
        num1,num2,num3 = int(num1), int(num2), int(num3)
        if num1>=num2 and num1>=num3:
            return num1
        elif num2>=num1 and num2>=num3:
            return num2
        else:
            return num3
print(max_num(num1,num2,num3))