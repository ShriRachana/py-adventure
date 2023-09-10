#except for cathing errors

try:
    value = 10/0
    num = int(input("Enter number :  "))
    print(num)
except ZeroDivisionError as err: 
    print(err)
except ValueError:
    print("Invalid input")