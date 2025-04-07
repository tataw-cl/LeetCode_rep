# 229. Majority Element II
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow up: Could you solve the problem in linear time and in O(1) space?


#My Solution:
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        elements=defaultdict(int)
        n=len(nums)
        ratio=n//3
        res=[]
        for num in nums:
            elements[num]+=1
        for num in elements:
            if elements[num]>ratio:
                res.append(num)

        return res


        #Time complexity: O(n)
        #Space complexity: O(n)


        #Other Solutions:
        #Boyer-Moore Voting Algorithm
        #The Boyer-Moore Voting Algorithm is an efficient algorithm for finding the majority element in an array.
        #In this case, we can extend the algorithm to find all elements that appear more than n/3 times.
        #The algorithm works by maintaining two potential candidates and their respective counts.
        #If the count of a candidate reaches zero, we replace it with the current element and reset the count.
        #Finally, we verify the candidates by counting their occurrences in the array.
        #This algorithm runs in O(n) time and uses O(1) space.

        #Implementation:
        class Solution:
            def majorityElement(self, nums):
                if not nums:
                    return []

                # Step 1: Find potential candidates
                candidate1, candidate2, count1, count2 = None, None, 0, 0

                for num in nums:
                    if num == candidate1:
                        count1 += 1
                    elif num == candidate2:
                        count2 += 1
                    elif count1 == 0:
                        candidate1, count1 = num, 1
                    elif count2 == 0:
                        candidate2, count2 = num, 1
                    else:
                        count1 -= 1
                        count2 -= 1

                # Step 2: Verify the candidates
                count1, count2 = 0, 0
                for num in nums:
                    if num == candidate1:
                        count1 += 1
                    elif num == candidate2:
                        count2 += 1

                result = []
                if count1 > len(nums) // 3:
                    result.append(candidate1)
                if count2 > len(nums) // 3:
                    result.append(candidate2)

                return result
            
            #Time complexity: O(n)
            #Space complexity: O(1)