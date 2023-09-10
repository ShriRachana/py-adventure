employee_file = open("ProjectGiraffe/employee.txt", "r")
print(employee_file.readable())
print(employee_file.writable())
employee_file = open("ProjectGiraffe/employee.txt", "r+")
print(employee_file.writable())
#print(employee_file.read())
for employee in employee_file.readlines():
    print(employee)
#print(employee_file.readlines())
#print(employee_file.readline())

employee_file.write("\nToby - HR")
employee_file = open("ProjectGiraffe/employee.txt", "w")
employee_file.write("\nRita - Legal")
#employee_file.close()

employee_file = open("ProjectGiraffe/employee1.txt", "w")
employee_file.write("\nToby - HR")
employee_file.write("\nTony - HR")

employee_file = open("ProjectGiraffe/index.html", "w")
employee_file.write("<p>This is a HTML file</p>")