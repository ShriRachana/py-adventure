#class function : function inside a class that can modify the information inside the class or provide specific information about those objects. 


from student import student

student1 = student("oscar", "Accounting", 3.1)
student2 = student("Phyllis", "Business", 3.8)

print(student1.on_honor_roll())
print(student2.on_honor_roll())