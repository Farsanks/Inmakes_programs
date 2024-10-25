def function1(a,b):
    print(a/b)
try:
    a=5
    b=0
    print(a/b)
except:
    print("there is a divide by zero exception")
finally:
    print("there is no way")