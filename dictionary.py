x={"chair":500,"table":300,34:"python"}
print(x)
print(x["chair"])
print(len(x))
x["vegetables"]=120
print(x)
x.update({12:"django"})
print(x)
x.pop("table")
print(x)

for i in x.values():
    print(i)
for i in x.items():
    print(i)