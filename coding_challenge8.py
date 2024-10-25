def student_discount(price):
    price=price-(price*10)/100
    return  price
def regularbuyer_discount(newprice):
    newprice=newprice-(newprice*5)/100
    return newprice
product=input("enter the product name")
product_price=int(input("enter the product price"))
print(regularbuyer_discount(student_discount(product_price)))