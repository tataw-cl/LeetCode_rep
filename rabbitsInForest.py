# 781. Rabbits in Forest
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

# Given the array answers, return the minimum number of rabbits that could be in the forest.

 

# Example 1:

# Input: answers = [1,1,2]
# Output: 5
# Explanation:
# The two rabbits that answered "1" could both be the same color, say red.
# The rabbit that answered "2" can't be red or the answers would be inconsistent.
# Say the rabbit that answered "2" was blue.
# Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
# The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
# Example 2:

# Input: answers = [10,10,10]
# Output: 11
 

# Constraints:

# 1 <= answers.length <= 1000
# 0 <= answers[i] < 1000


#My Solution:
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        res=len(answers)
        extra = 0
        ans = defaultdict(int)
        for answer in answers:
            if answer != 0:
                if ans[answer] == 0:
                    extra += answer
                    ans[answer] = answer

                elif ans[answer] > 0:
                    extra -= 1
                    ans[answer] -= 1
                    if ans[answer] == 0:
                        ans[answer] = -1

                elif ans[answer] < 0:
                    extra += answer
                    ans[answer] = answer

        res += extra

        return res

        #Time Complexity: O(n)
        #Space Complexity: O(n) for the ans dictionary


#Other Solution:
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        from collections import Counter
        
        count = Counter(answers)
        total_rabbits = 0
        
        for answer, freq in count.items():
            # Calculate the number of groups needed
            groups = (freq + answer) // (answer + 1)
            total_rabbits += groups * (answer + 1)
        
        return total_rabbits
    
    #Time Complexity: O(n)
    #Space Complexity: O(n) for the Counter dictionary

