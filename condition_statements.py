#if is a block in python it is called suite
#we have to follow indentation in python

x=12
r= x%2

# nested if

if r==0:
    print("even")
    if x>10:
        print("number is greater than 10")
    else:
        print("number is less than 10")
else:
    print("odd")
print("exit")


