list = ["larrt", "harrt", "mart"]
list.append("cart")
print(list)
list.insert(0,"parrt")
print(list)
list.extend(["molly", "holly", "me"])
print(list)
print(list.index("molly"))

list.remove("holly")
print(list)
list.pop(1)
print(list)
print(list.append("yaya"))
## NO, does not work, append() returns None
print(list)
list1 = []
print(list1)
list1.append("4")
print(list1)

list2 = ['a','b','c','d']
print (list2[1: -1])
list2[0:2] = 'z'
print(list2)