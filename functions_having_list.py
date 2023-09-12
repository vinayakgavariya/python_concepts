
def count(list):
    even = 0
    odd = 0

    for i in list:
        if i%2==0:
            even=i+1
        else
            odd+=1
    return even,odd

list = [20,15,15,17,18,19]

even,odd = count(list)

print("Even : {} and Odd : {}".format(even,odd))


# today i learnt

#.format method on string 
#"Even : {} and Odd : {}": This is a string that serves as the format template for the output. The {} placeholders within the string are placeholders where values will be inserted.