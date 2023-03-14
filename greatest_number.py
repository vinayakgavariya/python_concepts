x=input("Enter first number:")
y=input("Enter second number:")
z=input("Enter third number:")

if x>y:
    if y>z:
        print("x is greatest number")
    else:
        if x>z:
            print("x is greatest number")

elif y>x:
    
    if x>z:
        print("y is greatest number")
    else:
        if y>z:
            print("y is greatest number")


if z>y:
    if y>x:
        print("z is greatest number")
    else:
        if z>x:
            print("z is greatest number")

