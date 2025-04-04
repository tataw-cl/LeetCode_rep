# 904. Fruit Into Baskets
# Solved
# Medium
# Topics
# Companies
# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

 

# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:

# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:

# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
 

# Constraints:

# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length

#My Solution:
class Solution(object):
    def totalFruits(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l=0
        res=0
        freqDict=defaultdict(int)
        for r in range(len(fruits)):
            freqDict[fruits[r]]+=1
            while len(freqDict)>2:
                freqDict[fruits[l]]-=1
                if freqDict[fruits[l]]==0:
                    del freqDict[fruits[l]]
                l+=1
            res=max(res,r-l+1)
        return res

        # Time complexity: O(n)
        # Space complexity: O(n)
        # where n is the number of fruits.


        #Other solution:
        class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        A=fruits
        maxfruit=0
        first=A[0]
        second=-1
        left=0
        right=0
        
        
        while right<len(fruits):
            # print(right,left,maxfruit,"Start")
            if A[right]==first:
                right+=1
                

            elif second==-1:
                second=A[right]
                right+=1
            elif A[right]==second:
                right+=1
            else:
                maxfruit=max(maxfruit,right-left)
                temp=right-1
                second=A[right]
                first=A[right-1]
                while A[temp]==first:
                    
                    temp-=1
                    
                left=temp+1
                
                # print(right,left,maxfruit,"Inside else")
                right+=1
        # print(maxfruit,"Start")
        return max(maxfruit,right-left)
    
    # Time complexity: O(n)
    # Space complexity: O(1)