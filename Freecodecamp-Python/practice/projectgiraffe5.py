lucky_number = [99,9989899,10,0, 4,5,6,78,99,10]
friends = ["kevin", "karen","Jim", "Oscar","Oscar","Oscar","Tim" ]
print(friends[:1])
print(friends)
friends[0] = "Mike"
print(friends[:1])
friends.extend(lucky_number)
friends.append("creed")
print(friends)
friends.insert(1, "kelly")
print(friends)
friends.remove("Jim")
print(friends)
#lucky_number.clear()
print(lucky_number)
print(friends)
friends.pop()
print(friends)
print(friends.index("karen"))
print(friends.count("Oscar"))
lucky_number.sort()
print(lucky_number)
lucky_number.reverse()
print(lucky_number)
friends2 = friends.copy()
print(friends2)