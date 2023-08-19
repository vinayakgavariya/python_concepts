#     return leap
def is_leap(year):
  leap = False

  if (year % 4 == 0) and (year % 100 != 0): 
      # Note that in your code the condition will be true if it is not..
      leap = True
  elif (year % 100 == 0) and (year % 400 != 0):
      leap = False
  elif (year % 400 == 0):
      # For some reason here you had False twice
      leap = True
  else:
      leap = False

  return leap

# things i learnt:-

# i confused the condtions of being a leap year divisible by 4 and 400 and 100 one
# i didn't included divisible by 4 and not divisible by 400 condition
year = int(input())
print(is_leap(year))