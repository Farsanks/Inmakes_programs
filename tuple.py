x=(12,13,"hello","python")
print(type(x))
print(x[1])
y=list(x)
print(y)
print(type(y))
y.insert(2,"hai")
print(y)
x=tuple(y)
print((x))