#Lesson 1 : Playing with Outputting data

print("Hello World")

#Drawing a shape wit Python 
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")

#Variables and Data types 
character_name =  "Jane"
character_age = 35.1
is_male = 'false'
print("There is a person named , " + character_name)
#We need to concatenate the o/p data using '+'
print(character_name + " She was " + str(character_age) + " years old")
#Different data types are : string, int, decimal, float, boolean (T/F)
character_name = "Shri Rachana"
print(character_name + " She works as a SDE in a cool company")
print("She does love crossfit")

#Lesson 2 : Working with strings
#New line is introduce with \n(backslash n)
print("Giraffe\nAcademy")
#Use backslash to help code print quotes or slashes 
print("Giraffe\"Academy")
phrase = "GIRAFFE Academy stored in a variable called phrase"
print(phrase)
#use concatenation to tie string together
print(phrase + " is cool yo")

#Lesson 3 : Function is nothing but a block of code that performs a SPECIFIC OPERATION for us. 
#Example : Modify our string or get information from our string 
#Example : Use function to do an action or operation on a string like make it all lower case. 

print(phrase.lower())
print(phrase.upper())
print(phrase.islower())
#Example : Use multiple functions to peform multiple operations together. 
print(phrase.upper().isupper())
