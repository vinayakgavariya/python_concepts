av = 5
x= int ( input("How many candies you want?"))

i = 1
while i <=x:

    if i>av:
        break

    print ("Candy")
    i+=1

print ("bye")

# print values from 1 to 100 and remove divisible by 3

for i in range (1, 101):

    if i %3==0:
        continue
    print (i)
print("bye")

'''

In Python, continue and pass are two different statements used in different contexts.

continue statement:

The continue statement is used within loops (such as for or while) to skip the current iteration and move to the next iteration.
When the continue statement is encountered, the code execution jumps to the next iteration of the loop, skipping any remaining statements within the loop block for that particular iteration.
The loop continues with the next iteration, and subsequent statements within the loop block are executed as usual.
Example:

python
Copy code
for i in range(5):
    if i == 2:
        continue
    print(i)

'''

'''
pass statement:

The pass statement is a placeholder statement that does nothing.
It is used when a statement is syntactically required but you don't want any specific code to be executed at that point.
It is commonly used as a placeholder in empty function definitions, class definitions, or conditional statements that will be implemented later.
Example:

python
Copy code
def my_function():
    pass  # Placeholder for the function body

if condition:
    pass  # Placeholder for the condition block
else:
    # Actual code for the else block
    print("Condition is false")
In the above example, pass acts as a placeholder that allows the code to be syntactically correct. It signifies that no specific action is required at that point.

'''