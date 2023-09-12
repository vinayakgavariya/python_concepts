#scope in function

a= 10  #global variable

def sothing():
    a=15      #local vairiable
    b=8
    print(a)
sothing()

print(a)


#using global variable inside function

a=10
b=9

def something():

    global a

    x = globals(['a'])  # will give access of all the global variables
    print(id(x))
    # a = 15

    print("in fun ", a)
    globals() ['a'] = 15

    # a = 9

something()

