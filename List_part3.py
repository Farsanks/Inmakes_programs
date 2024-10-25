#append
fruits=["apple","orange","pinapple"]
fruits.append("cherry")
print(fruits)
#insert
fruits.insert(1,"grapes")
print(fruits)
print(len(fruits))
print(fruits.index("cherry"))
fruits=["apple","orange","pinapple"]
fruits.remove("orange")
print(fruits)
fruits.pop(1)
del fruits[0]
print(fruits)
fruits.clear()
