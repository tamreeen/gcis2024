import random
import time

"""DONE BY GROUP 6: TAMREENN , ZIAD , RIBBIYOON -  THE WHOLE GROUP WORKED ON EACH PART TOGETHER"""

# Phase 1: Insertion Sort:
""" first you swap the places of elements by using the index, u store index a in a variable called temp so u can place
index b in a's previous location, basically you are swapping both the elements by calling out their index"""
def swap(an_array, a, b):
  
    temp = an_array[a]
    an_array[a] = an_array[b]
    an_array[b] = temp

"""If the element at the current index is smaller than the element to its left, it will be swapped, it will continue moving the 
element backward until it is in the correct position in the sorted part ."""
def shift(an_array, index):
            
     while index > 0:
        if an_array[index] < an_array[index - 1]:
            swap(an_array, index, index - 1)
        index -= 1
""" range function is used to go through each element in the array and sort it by calling out the shift function, inside the
shift function, it contains the swap function"""

def insertion_sort(an_array):
   
    for each_index in range(len(an_array)):
        shift(an_array, each_index)
    return an_array

def generate_sorted_data(size):
    
    data = [] # empty list to store the random values
    for i in range(size):
        random_value = random.randint(1, 100) # randint will produce random integers from 1 to 99
        data.append(random_value) # append will add the values to the data container
    
    return insertion_sort(data)

# phase 1 is completed

# Phase 2: Binary Search

def binary_search(an_array,target,start=None,end=None):
    if start==None: # if start is none then it's value will be zero
        start=0
    if end==None:
        end=len(an_array)-1 # if end is none it will be the last number of the array
    if start>end: # to stop searching  
        return None
    else:
        mid=(start+end)//2 # mid is the midpoint, the value of start and value of end will be divided by 2
        if target==an_array[mid]: # if the answer u get after dividing matches the target value then that is your midpoint
            return mid
        
 #but if the answer u get is smaller then target then u search for the target again
 # your start number will be the number that comes after the midpoint  (mid +1)    
 # your end number will be the last number        
        elif an_array[mid]<target: 
            return binary_search(an_array,target,mid+1,end)
#but if the answer u get bigger then target then u search for the target again
#must be in the first half of the array (the left side)
#So our starting value will be the start to just before the midpoint (mid - 1).
        else:
            return binary_search(an_array,target,start,mid-1)

""" phase 2 is completed"""
# phase 3 starts

def merge_sort(an_array):
    # if the array has 1 element then return the array because it is sorted
    if len(an_array) <= 1:
        return an_array
    else: # split the array into 2 halfs, one container is called half1 and another container is called half2
       half1, half2 = split(an_array)
       return merge(merge_sort(half1), merge_sort(half2)) # the merge function will be called to merge the containers together

def split(an_array):
    # this function will split the array into 2 halfs by dividing with 2
    mid = len(an_array) // 2
    half1 = an_array[:mid] # half 1 will contain the values from the start till the midpoint
    half2 = an_array[mid:] # half 2 will contain the values from the midpoint till the end
    return half1, half2 # will return the containers

def merge(sorted1, sorted2):
    # this function will merge the containers
    result = []  # to store the final array
    i1 = 0  # index of first value
    i2 = 0  # index of second value
    while i1 < len(sorted1) and i2 < len(sorted2):  # both sorted list should have values so we can compare
        if sorted1[i1] <= sorted2[i2]:  # if sorted1 is smaller or equal to sorted2 then we will add it to result by using append function
            result.append(sorted1[i1])  # append function will allow us to add the values to result
            i1 += 1  # to go to next element in array
        else:
            result.append(sorted2[i2])  # if sorted1 is bigger or equal to sorted2
            i2 += 1
    # if there is remaining elements
    while i1 < len(sorted1):
        result.append(sorted1[i1])
        i1 += 1
    
    # if there is remaining elements
    while i2 < len(sorted2):
        result.append(sorted2[i2])
        i2 += 1
    
    return result

# phase 3 is completed

# phase 4:

def linear_search(an_array, target):
    """ will go through each item in the array by using range function"""
    for i in range(len(an_array)):
        if an_array[i] == target: # if current item matches the target we are looking for it will return i
            return i
    return None  # target not found

# Timing:

def linear_search_timer(an_array, target):
    #Measure the time it takes to perform linear search.
    begin = time.perf_counter() # time will start
    result = linear_search(an_array, target)
    end = time.perf_counter() # once the word is found, the completion time will be shown
    elapsed = end - begin # subtract the time to find the amount of time taken
    print("this is Linear Search, Found at index", result, "and the Time taken:", elapsed)

    return elapsed

def binary_search_timer(an_array, target):
    #Measure the time it takes to perform binary  search.
    begin = time.perf_counter()
    result = binary_search(an_array, target)
    end = time.perf_counter()
    elapsed = end - begin
  
    print("this is binary search, Found at index", result, "and the time taken is:", elapsed)
    return elapsed

"""
ANSWERS FOR REFLECTION QUESTION: 

In a linear search, we have to check each and every item to see if it matches the target so if you have more then 100 
values in your array it will take such a long time but with binary search, it splits the array into 2 smaller arrays and 
one of the arrays will be ignored if it does not contain the target value, using binary search is more faster then 
linear search

sorting algorithm is important for the performance of search algorithms, especially in phase 4 where we
compared binary search to linear search. Binary search is faster and efficient when the data is sorted 
because we only have to half the array, so we do not need to check each and every element in the array 
which reduces the time to search for the target, however in linear search, it checks each element one by one,
which takes a lot of time and if there is a lot of elements, it will be less efficient. If the data is not 
sorted then we have to use linear search, because binary search only worked in sorted arrays

Merge Sort or  Quick Sort have a time complexity of O(n log n), meaning they sort large datasets much faster than 
Bubble Sort or Insertion Sort which take O(n²)time . and binary search operates in logarithmic time once the algorithm is
sorted

""" 
def main():
   
# phase 1 output
    size = int(input("What size do you want for your array? "))  # ask the size of the array
    sorted_data = generate_sorted_data(size)  
    print("Sorted data:", sorted_data)
# phase 1 is completed

# phase 2:
    target = int(input("enter one of the values from the previous array: "))
    index = binary_search(sorted_data, target)
   
    if index is not None:
        print(target, "is in at index:" , index)
    else:
       print(target, "not found")

    # Searching for a target that doesn't exist in the array
    target_not_found = int(input("enter one of the values that is not available in the previous array:"))
    index_not_found = binary_search(sorted_data, target_not_found)

    if index_not_found is not None:
       # print(target_not_found, "not found", "so", index, "is not available")
         print(target, "is in at index:" , index)
    else:
       # print(target, "is in at index:" , index) 
        print(target_not_found,"is not available")
        
  # PHASE 3
    large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for _ in range(990)]


    print("First 10 elements before sorting:")
    for i in range(10):
        print(large_data[i], end=' ')  # Print first 10 elements on the same line


    large_data.sort()  # 'large_data' list will be sort in place, which is destructive

    print("\nFirst 10 elements after sorting:") #\n is for new line
    for i in range(10):
       print(large_data[i], end=' ')  # end is used to print values in same line

# PHASE 4
    target = 72  # Sample target
    print("\nwe will find how long it takes to find target:",target  )
    linear_search_timer(large_data, target)
    binary_search_timer(large_data, target)

  
if __name__ == "__main__":
    main()
