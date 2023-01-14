#function keyword : def funcname():
#code inside a function is indentended by 4 spaces
#paramaeters acan be passed inside a function- data to the func that the function can use
#sometimes functions give information returns values back so we use return to do this. 
print("Top-top")
def say_hi(name, age):
    print("Hiya "+ name + "you are " + str(age))
print("Top")
say_hi("Rach", 31)
say_hi("Mike", 32)
print("bottom")

def cube_num(num):
    num*num*num

print(cube_num(3))

def cube_num_val(num):
    print("nada")
    return num*num*num
    print("yada")

result = cube_num_val(4)
print(result)