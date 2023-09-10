#Humans use if statements all through the day, this helps the computer decide which part of the code to execute
#scenario : 
#I wake up 
#if I am hungry 
#    I eat breakfast 

#I leave my house : 
#If Its cloudy 
#    I gring an umbrella 
#otherwise 
#    I bring sunglasses. 

#Im at a restarurant 
#if I want meat 
#   I order a steak
#otherwise if I want pasta
#    I order spag and meatballs 
#otherwise
#    I order a salad

def find_gender_height():
    is_male = False
    is_tall = False

    if is_male and is_tall: 
        print("You are a male")
    elif not is_male and is_tall:
        print("You are a tall female")
    elif is_male and not is_tall:
        print("You are a short male")
    else:
        print("You are female")

find_gender_height()
