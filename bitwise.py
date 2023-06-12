"""
BITWISE OPERATOR

something to be done with binary numbers

Complement ( tilde ~)

"""


#Compliment 
# we never store negative numbers in system we store positive numbers and negative numbers are converted into positive numbers

# 2`s compliment = 1`compl+1 

a= ~45
print (a)
print(bin(45))

"""
Certainly! Let's break down the binary addition of 101101 + 1 step by step:

markdown
Copy code
   1 0 1 1 0 1   <- 101101
+           1   <- 1
-----------------
We start from the rightmost bit, which is the least significant bit (LSB). In this case, the rightmost bit of the first number is 1, and we add it to the rightmost bit of the second number, which is also 1.

markdown
Copy code
   1 0 1 1 0 1   <- 101101
+           1   <-     1
-----------------
             0   <- Sum: 0, Carry: 1
The sum of 1 + 1 is 0, and we have a carry of 1 to the next bit.

Moving to the next bit to the left, we add the next pair of bits:

markdown
Copy code
   1 0 1 1 0 1   <- 101101
+           1   <-     1
-----------------
           0     <- Sum: 0, Carry: 1
Again, the sum of 1 + 1 is 0, and we carry 1 to the next bit.

Continuing this process for each pair of bits, we get:

yaml
Copy code
   1 0 1 1 0 1   <- 101101
+           1   <-     1
-----------------
         0       <- Sum: 0, Carry: 1
       1         <- Sum: 1, Carry: 0
     1           <- Sum: 1, Carry: 0
   0             <- Sum: 0, Carry: 1
  1              <- Sum: 1, Carry: 0
1                <- Sum: 1, Carry: 0
After adding all the bits, we obtain the result:

markdown
Copy code
   1 0 1 1 0 1   <- 101101
+           1   <-     1
-----------------
   1 0 1 1 1 0   <- 101110
So, the binary addition of 101101 + 1 equals 101110.

"""


# AND bitwise

a= 12 & 13
print (a)

# first convert both into binary then 

""""
00110000

0000 1100
             12 &
             13
00001101

00001100     12

"""

ex= (25 & 30)
print(ex)

# XOR bitwise ^ 

xor= 12^13
print(xor)

# LEFT SHIFT

"""
1010.000
shift by 2 bit ( that means shift ADD two zeros at the end)
101000.00
"""

# RIGHT SHIFT 

# we will be loose bits 

"""
1010.000
shift by 2 bit ( that means shift REMOVE two zeros at the end)
10
"""




