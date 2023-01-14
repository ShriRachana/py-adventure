x = 100
def f():
    #global makes the scope of x 'global' to the program
    global x
    x += 1
    print(x)

f()