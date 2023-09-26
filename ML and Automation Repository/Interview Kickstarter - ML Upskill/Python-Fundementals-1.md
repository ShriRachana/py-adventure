# Agenda 
Go through the basics of Python to be able to start translating actions I want to system to do into code. 

### Sub-Note 
Python Fundamentals - 1 Class Slides & Notes (Dated : Jun2 22,2023)

## Basic programming condepts with Python 
1. Variables 
2. Data Types(&typecasting) conversion of one data type into another is typecasting/typeconversion in python.
    - Python supports a variety of functions or methods like int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. 
3. Operators (+,-)
4. Logical operators 
5. If statements
6. Loops(for-while)
7. Functions
8. Scope of Variables
9. Python Modules

## For executions use one of the below tools 
1. IDE - visual studio code
2. IDE - Pycharm
3. Jupyter Notebook 
4. JupyterLab
5. Google collab 

## Leetcode
1. Two Sum 
26. Remove Duplicated from Sorted Array 
27. Remove Element 
217. Contains Duplicate 

## Python for Machine Learning

### Simple and consistent 
- Python's simplicity allows developer to write reliable systems. 
- Developers get to put all the effort into solving and ML problem instead of focussing on the technical nuances of the language. 
- Python was designed for readability. '
- It is easier to learn and use to develop modeles for machine learning. 
### Libraries and frameworks variety 
- Python frameworks and libraries offer a reliable environment that reduces software development tine significantly. 
### Independence across platforms 
- Python runs across different platforms, which allows developer to develop as the only language and save time and resource for developers. 
### Great community and popularity 
- Python developer exchange forums are active in promoting the growth of the AI community as a whole. 

## Variable 
- Variables are contained for storing data values 
    - Python has no command for declaring a variable 
    - A variable is cretaed the moment you first assigb a value to it. 
    - Variables do not need to be declarred with any paticular 'type' and can even change type after they have been set. 
    - Casting can help specify or change type of a variable 
    - variable names are case-sensitive 

- Examples : 
    - a = 10 #integer 
    - b = 6.8 #float 
    - c1 = 'matt' #string 
    - c2 = "Shri" #string 
    - d = True #boolean (True/False) 
- Other Examples : 
    - a = 1 
    - A = "Hello World" 
    - print(a, type(a)) 
    - print(A, type(A)
- Good to know : 
    - How to check variable’s type? 
    - How to change variable’s type? 
    - How to define a positive or negative infinity? 
    - How to convert float to int in floor and ceil?

### Camel Case 
- Each word, except the first, starts with a capital letter:
    - exampleVariableName 

### Pascal Case 
- Each word, except the first, starts with a capital letter:
    - exampleVariableName

### Snake Case 
- Each word, except the first, starts with a capital letter:
    - exampleVariableName


## Example : Reverse an array 
 - Reverse An Array- Reverse a given list of numbers.
 - Example 1 : {"nums": [50, 35, 78, 66, 17]} || Output: [17, 66, 78, 35, 50]
 - Example 2: {"nums": [50, 40, 30, 20]} || Output: [20, 30, 40, 50]
    - Notes: Modify the input array in-place and return the modified array.
    - Constraints:
        - 1 <= size of the input array <= 106
        - 0 <= any element of the input array <= 106
- [**code-snippet**](https://github.com/ShriRachana/py-adventure/blob/a72cd1c8a2b87bfa97ad6768488baf7a469d2e32/ML%20and%20Automation%20Repository/Interview%20Kickstarter%20-%20ML%20Upskill/reverse-an-array.py)
https://github.com/ShriRachana/py-adventure/blob/a72cd1c8a2b87bfa97ad6768488baf7a469d2e32/ML%20and%20Automation%20Repository/Interview%20Kickstarter%20-%20ML%20Upskill/reverse-an-array.py#L34-L42