# code with harry https://www.youtube.com/watch?v=0INvoK_T0cE

#strings are immutable

#all methods are applied and new strings get created

a="Vinayak!! !!!!!!!! Harry"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))  # remove trailing ! 
print(a.replace("Vinayak", "John"))
print(a.split(" ")) # split converts string into list

blogHeading = "intro tO python"
print(blogHeading.capitalize())  # really helpful to convert first letter in upper case

str1="Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50))) #makes it center

print((str1))
print((str1.center(50)))

print(a.count("Vinayak"))   #counts string

str1= "Welcome to the Console !!!"
print(str1.endswith("!!!"))

# we can overwrite variable in python
str1= "Welcome to the Console !!!"
print(str1.endswith("to", 4,10))

str1= "He's name is Dan. He is an honest man!!!"
print(str1.find("is")) # will give index of is
print (str1.index("ishh"))  # gives exception error

#isalnum():

str1= "WelcomeToTheConsole"
print(isalnum())

str1="Welcome"
print(str1.isalpha())

str1="hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1)
print(str1.isprintable()) # \n is not printable hence false

str1="      "  #using spacebar

str2="          "  #using tab
print(str2.isspace())

str1= "World Health Organization"
print(str1.istitle())

str2 = "To kill a Bird"
print(str2.istitle())  # capitalize the first word

str3 = "Python is a Interpreted Language"
print(str3.swapcase())  # swaps the case

str1= "His name is John. John is an honest man"
print(str1.title())   