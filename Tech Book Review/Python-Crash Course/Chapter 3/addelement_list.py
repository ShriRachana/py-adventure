motorcycles =["yamaha", "suziki", "bmw", "BMW"]
print(motorcycles)
motorcycles.append("Ducati")
print(motorcycles)
motorcycles[0] = "yellow taxi"
print(motorcycles)


fruits = []
print(fruits)
fruits.append("orange")
fruits.append("berries")
print(fruits)
fruits.insert(2, "mango")
print(fruits)
del fruits[0]
print(fruits)
fruits.pop()
print(fruits)
fruits.pop()
print(fruits)

estudents = ["Jack", "Black","Black","Black", "Ryan", "Brian"]
print(estudents)
print(estudents.remove('Black'))
print(estudents)
estudents.sort()
print(estudents)
estudents.sort(reverse=True)
print(estudents)
print(sorted(estudents))
estudents.reverse()
print(estudents)
print(len(estudents))
