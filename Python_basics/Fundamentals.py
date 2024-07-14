#variable declaration in python
a = 10
b,c = 20, "abc"
d=0
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
#incrementing in python
#n=n+1, n+=1
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
#Null==None in python
#------------------------------------------------------------------------------------------

#if statements in python
if a<10:
    print("a<10")
else:
    print("a is not less than 10")
#------------------------------------------------------------------------------------------
#Logical AND in python == 'and' and OR == 'or'
#------------------------------------------------------------------------------------------
#Using multiline conditionals in python
if((a>2 and a!=b) or a==b):
    a+=2
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
#while loops in python
while d<5:
    print(d)
    d+=1
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
#for loops in python
#Looping from i=0 and increasing i till i<10 and ending there
for i in range(10):
    print(i*i)    
#looping from i=a, and increasing i till i<20
for i in range(a,20):
    print(i)
#Looping from i=5 and decreasing till i>0(i.e i=1) and ending there
for i in range(5,0,-1):
    print(i)
    #here, we use the -1 to indicate that the loop should decrement by 1.
    #We can replace -1 by any other number to decrement by the value.
    #If we do not include any third parameter, the loop will increment by default
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
#Division in python. By default, using the division sign(/) uses decimal or floating point division
b/a # result=2.0 for a=10 and b=20
#To do intege division in python, we use the double division. i.e (//) to round down values to their integers
b//a # result=2 for a=10 and b=20
#Careful:most languages round towards 0, but by default negative numbers will round down. i.e -3//2 = -2
# A workaround for this is to use decimal division, then convert to int
# i.e print(int(-3/2))
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
# some math helpers from the math library include the 'floor,ceil,sqrt' functions
# e.g print(math.floor(3/2))
# print(math.ceil(3/2))
# print(math.sqrt(2))
# print(math.pow(2, 3)) 2^3(2 raised to the power of 3)
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
# Obtaining max and min integers, we use
#  float("inf") maximum integer
# float(-inf) minimum integer
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
#Arrays in python. Arrays are also called lists in python
arr = [0,1,2]
print(arr) #will print [0,1,2]
#Arrays in python are dynamic arrays and can be used as a stack. So, we can append(push) amd pop(pop) to and from the array. e.g
arr.append(4)
arr.append(5)
print(arr)
# will print [0,1,2,4,5]
arr.pop()
print(arr)
# will print [0,1,2,4]
#we can insert into the middle of an array with complexity of Big O(n)
arr.insert(3,3)# Will print [0,1,2,3,4]
# Will insert 3 at array index 3 and shift the remaining element's 1 position to the right
# We can do normal indexing of arrays
print(arr[2])
arr[4]=5
#When indexing arrays, -1 is not out of bounds and will return the value in the last index of the array, -2 second to the last and so on... 
print(arr[-1]) # will return arr[4]==5
print(arr[-2]) # will return arr[3]==3
#initializing an array of size n with all default values of 1
n=5
arr1=[1] * n
print(arr1)
#Will print [1,1,1,1,1]
print(len(arr1)) # will print 5

#Sublists (slicing an array)
#printing the values of the array from index 1 to index 2, not including index 3
print(arr1[1:3]) # Will print indexes 1,2
#printing from index 0 to index 4 not including index 5
print(arr1[0:5]) #will print inidexes 0,1,2,3,4. Actually similar to for loops with the last index being exclusive

#unpacking in arrays is assigning the individual elements of the array to some other variables
x,y,z=[1,2,3]
print(x, y, z) # will print 1 2 3
#Warning: The number of variables on both sides should match. a,b=[1,2,3] will return an error

#Looping through an array
#method 1. Access with index
num=[1,2,3,4,5]
for i in range(len(num)):
    print(num[i]) # Will print 1 2 3 4 5

#method 2. Access values without index
for n in num:
    print(n) # Will print 1 2 3 4 5

#Method 3. Access index and value
for i,n in enumerate(num):
    print(i,n)

#Looping through multiple arrays simultaneously and combining the pairs
nums1=[1,2,3,4]
nums2=[5,6,7,8]
for n1,n2 in zip(nums1, nums2):
    print(n1,n2)
# Will print:
# 1 5
# 2 6
# 3 7
# 4 8

#Reversing an array is done using the reverse method
nums1.reverse() #Reverses the contents of the array nums1
print(nums1) # Will print 4 3 2 1 

#Sorting an array
nums2.sort() #Sorts the array in ascending order
print(nums2)
#To sort in reverse order(descending order)
nums2.sort(reverse=True) # Will sort the array in descending order
print(nums2)
#Sort an array of strings
names=["bob", "Angela" "mary", "Steve"]
names.sort() # Will sort the names in ascending order, i.e letter-wise
print(names) # Will print [Angela, bob, mary, Steve]
# We could implement custom sorts, e.g by length
names.sort(key=lambda x: len(x)) #Sorts the names array in terms of the length returned
# by the lambda function which checks each strings length and then sorts the array by length in ascending order

#List Comprehension
arr=[i for i in range(5)] # to initialize the array with numbers from 0 to 4 and include them in the array. i.e arr=[0,1,2,3,4]

#Creating a 2D list
# A 2D list is a list of lists
arr2D=[[1,2,3],[4,5,6],[7,8,9]]
arr = [[0]*3 for i in range(3)] # Will create a 3x3 2D array with all elements initialized to 0 
#------------------------------------------------------------------------------------------

#Strings in python
s="Hello"
print(s[0]) # Will print H
#We can slice strings as we do with arrays
print(s[1:3]) # Will print el
#Strings are immutable in python, so we cannot change the value of a string at a particular index
#We can concatenate strings using the '+' operator
s1="world"
s2=s+s1 # Will concatenate the strings s and s1 and store the result in s2
#Strings can be converted to integers and vice versa
s="123"
n=int(s) # Will convert the string to an integer
s=str(n) # Will convert the integer to a string
#We can access the ASCII value of a character using the ord function
print(ord("a"))
#Combining strings with empty delimiters
strings=["ab", "cd", "ef"]
print("".join(strings))#Will print abcdef
#------------------------------------------------------------------------------------------
# Queues in python are double ended by default and can be used by...
from collections import deque
queue=deque()
queue.append(1)
queue.append(2)
print(queue)
#Queue operations
queue.popleft() #Removes elements from the left side of the queue
queue.appendleft(5) #Adds 5 to the left of the queue
#To pop from the right side, we use the normal pop operation
#------------------------------------------------------------------------------------------

#Hashsets in python || hashsets operations are usually done in O(1) time complexity
mySet= set() # Hashsets cannot have repeated values
mySet.add(1) #Adds 1 to the hashset
mySet.add(2) #Adds 1 to the hashset
mySet.add(5)
print(mySet) # Will print {1,2,5}
print(len(mySet)) # prints 3
print(1 in mySet) # Will return True since there is 1 in the Hashset
print(2 in mySet) # Will return True since there is 2 in the Hashset
print(3 in mySet) # Will return False since there is no 3 in the Hashset
mySet.remove(2) # Used to remove 2 from the Hashset

#List to set
print(set([1,2,3])) # Will print 1,2,3
#set comprehension
mySet={i for i in range(5)}
print(mySet) # Will print 0,1,2,3,4
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
#HashMap(dictionaries (or Dics for short))
myMap={}
myMap["alice"]=88 #Assigns 88 to the key index alice
myMap["joe"]=84 #Assigns 84 to the key index joe
myMap["Bob"]=78
print(len(myMap))
print(myMap) # Will print {'alice':88, 'joe':84, 'Bob':78}
print(myMap["alice"]) # Will print 88
myMap["alice"]=80 #Will reassign key alice to value 80
print("alice" in myMap) #Will print true since alice is found in myMap Hashset
myMap.pop("alice") #Will delete the key alice and it's value
print("alice" in myMap) #Will print false since alice is now no longer found in myMap Hashset
#HashMap initialization
newMap={"jane": 70, "peter": 50, "James": 45}
print(newMap) #Will print {'jane': 70, 'peter': 50, 'james':45}

#Dics comprehension(Usaully used in graph problems in adjacency lists)
myMap={i: 2*i for i in range(3)}
print(myMap) #Will print {0: 0, 1: 2, 2: 4}

#Looping through maps
#Method 1. Using the map indexes, or a key
newMap={"jane": 70, "peter": 50, "James": 45}
for key in newMap:
    print(key, newMap[key]) #Will print: 
    # jane 70
    # peter 50
    # James 45
#method 2. Using the direct values
for val in newMap.values():
    print(val)# Will print:
    # 70
    # 50
    # 45
#method 3. Using unpacking to get the key and values
for key, val in newMap.items():
    print(key, val) #Will print 
    # jane 70
    # peter 50
    # James 45
    #------------------------------------------------------------------------------------------

    #------------------------------------------------------------------------------------------
    #Tuples in python
    #tuple initialization
    tup=(1,2,3) 
    #Tuples are immutable, so we cannot change the value of a tuple at a particular index
    tup[1]=5 # Will return an error
    tup[1] # Will return 2
    #Tuples can be used as keys in dictionaries(hashmaps)
    myMap={(1,2): 5, (2,3): 6}
    print(myMap[(1,2)]) # Will print 5
    #Tuples can be used as values in dictionaries
    myMap={1: (2,3), 2: (3,4)}
    print(myMap[1]) # Will print (2,3)
    #Tuples can be unpacked
    x,y=(1,2)
    print(x) # Will print 1
    #Tuples can be used to return multiple values from a function
    def func():
        return 1,2
    x,y=func()
    print(x) # Will print 1
    #------------------------------------------------------------------------------------------

    #------------------------------------------------------------------------------------------
    #Heaps in python
    import heapq
    #Heaps under the hood are arrays, but they are treated as binary trees
    #heap initialization
    heap=[]
    #Adding elements to the heap
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 2)
    heapq.heappush(heap, 3)
    print(heap) # Will print [1,2,3]
    #Popping elements from the heap
    print(heapq.heappop(heap)) # Will print 1
    print(heap) # Will print [2,3]
    #To get the minimum element in the heap
    #heap[0] will return the minimum element in the heap
    print(heap[0]) # Will print 2
    #minimum value in the heap is always at the root(index 0) of the heap
    #To get the maximum element in the heap, we use the nlargest method
    print(heapq.nlargest(1, heap)) # Will print [3] since 3 is the largest element in the heap
    #To get the minimum element in the heap, we use the nsmallest method
    print(heapq.nsmallest(1, heap)) # Will print [2] since 2 is the smallest element in the heap
    #Trying to implement a maxHeap in python
    maxHeap=[]
    heapq.heappush(maxHeap, -1) # Will push -1 to the heap
    heapq.heappush(maxHeap, -2) # Will push -2 to the heap
    heapq.heappush(maxHeap, -3) # Will push -3 to the heap
    print(maxHeap) # Will print [-3,-2,-1] since the heap is a minHeap
    #To implement a maxHeap, we can use the negative values of the elements and then negate(multiply by -1) the result
    #To get the maximum element in the maxHeap
    print(-1*maxHeap[0]) # Will print 3

    #Building a heap from an array
    arr=[1,2,3,4,5]
    heapq.heapify(arr) # Will convert the array into a heap
    #------------------------------------------------------------------------------------------

    #------------------------------------------------------------------------------------------
    #Functions in python
    #general look. We use the def keyword
    def myFunc(n,m):
        return n+m
    #To call the function
    print(myFunc(1,2)) # Will print 3

    #Nested functions in python
    def outerFunc():
        def innerFunc():
            print("Inner function")
        innerFunc()
#Functions can modify objects without reassigning unless using the nonlocal keyword
def double(arr, val):
    def helper():
        #Modifying array works
        for i,n in enumerate(arr):
            arr[i]*= 2
#Will only modify the value in the scope of the helper function
#To modify the value of a function in the helper function, we use the nonlocal keyword. e.g
        nonlocal val
        val*=2
 #------------------------------------------------------------------------------------------

  #------------------------------------------------------------------------------------------
  #Classes in python
  class MyClass:
    #Constructors
    def __init__(self,nums):
        #Creating member variables
        self.nums = nums