#sepcial type that allows us to loop through special items/collection. 
for letter in "Giraffe academy":
    print(letter)

friends = ["Jim", "Jordan", "Peele"]
for i in friends:
    print(i)
    print (len(i))

for index in range(2):
    print(index)

for index in range(len(friends)):
    print(friends[index])

print(2**3)

def raise_t0_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result*base_num
    return result

print(raise_t0_power(3,3))