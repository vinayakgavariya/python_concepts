english=input(int())

english_roll = set(map(int, input().split()))

french=input(int())

french_roll=set(map(int, input().split()))

print(english)
print(english_roll)
print(french)
print(french_roll)    

total=english_roll.union(french_roll)

print(len(total))
