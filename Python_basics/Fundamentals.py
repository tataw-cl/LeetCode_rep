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
    #We can replace 1 by any other number to decrement by the value.
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
print(arr1[0:5]) #will print inidexes 0,1,2,3,4. Actually similar to for loops with thye last index being exclusive

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
  
#------------------------------------------------------------------------------------------