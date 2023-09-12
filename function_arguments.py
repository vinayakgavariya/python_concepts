def update(x):
    x = 8
    print(x)

a=10   
update(a)

# not present in python:-
# pass by reference
# pass by value

def update (x):
    print(id(x))

def add(a,b):  #formal argument
    c=a+b
    print(c)

add(5,6)      #actual argument

#Types of Actual Argument

#postion
#keyword
#default
#variable length

#positions are imp in functions and if we don't know the postions we can use the keywords

def person (name,age):
    print(name)
    print(age)
person(age=28, name='navin')

#default

def person (name,age=18):
    print(name)
    print(age)
person('navin')

#variable length argument

def sum(a,*b): #b will have multiple values
    c = a+b
    print(c)
sum(5,6,78)

