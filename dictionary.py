#DICTIONARY

#IT HAS KEY-VALUE PAIR
#KEY SHOULD BE IMMUTABLE TYPE


dictionary ={1:"Abdul", 2:"Abhishek"}
print(dictionary)

#FETCH VALUE

print(dictionary[2])
# print(dictionary[3]) #doesn't exist gives error


#CLEAR

# clear=dictionary.clear
# print(clear)

#GET

print(dictionary.get(3)) #will not give error 

#we can get something for something doesn't exist
print(dictionary.get(3, "not found")) 

#CREATING DICTIONARY WITH TWO LISTS
#MERGING TWO LISTS IN A DICTIONARY

keys=['Abdul', 'Ameya', 'Abhishek']
values=['Boy', 'Girl', 'Boy']

data=dict(zip(keys,values))
print(data)

print(data['Abdul'])

#ADD ELEMENT IN DICTIONARY
data['Someone']='LGBTQ'
print(data)

#DELETE

del data['Someone']
print (data)

#NESTED DICTIONARY

language = {"JS":'Atom', "C++": "VS Code", "Python": ["Sublime","Pycharm"], "JAVA":{"JSE":'Netbeans', 'JEE':'Eclipse'}}
print(language)
print(language['JS'])
print(language['JAVA'])
print(language['JAVA']['JEE'])







