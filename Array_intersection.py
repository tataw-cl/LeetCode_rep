from collections import Counter
def intersect(nums1, nums2):
   count1=Counter(nums1)
   count2=Counter(nums2)
   intersection=count1&count2
   result=[]
   for num in intersection:
      result+=[num]*intersection[num]
   return result
# Example
nums1 = [1,2,2.3,5,1]
nums2 = [2,2,5]
print(intersect(nums1, nums2)) # Output: [2,2]