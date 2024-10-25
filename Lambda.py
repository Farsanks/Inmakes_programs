lambda  arguments :expression#syntax for lambda
x=lambda a,b,c:a+b-c
print(x(2,3,5))
def fun(a):
    return lambda  b:b-a
x=fun(2)
print(x(6))
y=lambda x:x*(x+89)**7
print(y(3))
