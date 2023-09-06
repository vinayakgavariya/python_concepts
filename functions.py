
# def function_name:
    #  print("Hello")

#defining a function
def geet():
    print("aditya <3.")

#calling a function
geet()

def add(x,y):
    c=x+y
    print(c)
add(5,4)

def add(x,y):
    c=x+y
    return c
result=add(5,4)
print("hello this is ex", result)

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result1, result2 = add_sub(5,4)
print(result)