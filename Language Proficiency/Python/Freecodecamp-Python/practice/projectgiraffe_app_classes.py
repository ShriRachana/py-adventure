#Classes and objects in python help make the program more organized and more powerful 
# strings, plain text, numbers, boolean value. Structures like list or dictionary 
# Example : Represent person, phonear etc
#To combat this, we use classes to create our own datatypes . Example : create a phone data type to represent a phone to store all information 
# about my phone in that data type. Classes help build data and functionality for it together and bundle it in a sense. 
# function inside a class is called a method in python 
#The name, gpa and such are attributes of the student data type defined below
class student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name 
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

