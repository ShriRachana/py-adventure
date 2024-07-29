#Object : represents the data and not just the blueprint(class)
#Object is teh instance of a class

from projectgiraffe_app_classes import student
student1 = student("Rick", "mba", 3.1, False)
student2 = student("Mal", "mba", 3.1, False)
student3 = student("Jim","Engg", 4.0, False)
print(student1.name)
print(student2.gpa)
print(student3.name, student3.gpa, student3.major, student3.is_on_probation)