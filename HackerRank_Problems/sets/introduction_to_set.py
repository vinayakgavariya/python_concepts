def average(array):
    # your code goes here
   # Calculate the sum of the elements in the array
   arr1=set(arr)
   print(arr1)
   total = sum(array)
        
   # Calculate the length of the array (number of elements)
   length = len(array)
   
   # Calculate the average by dividing the total by the length
   avg = total / length
   
   return avg  # Return the calculated average

        

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    result = average(arr)
    print(result)