# 649. Dota2 Senate
# Attempted
# Medium
# Topics
# Companies
# In the world of Dota2, there are two parties: the Radiant and the Dire.

# The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

# Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
# Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

# The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

# Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

 

# Example 1:

# Input: senate = "RD"
# Output: "Radiant"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
# Example 2:

# Input: senate = "RDD"
# Output: "Dire"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And the third senator comes from Dire and he can ban the first senator's right in round 1. 
# And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
 

# Constraints:

# n == senate.length
# 1 <= n <= 104
# senate[i] is either 'R' or 'D'.



#My Solution:
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        r = d = 0
        n = len(senate)
        for s in senate:
            if s == 'R':
                r += 1
            else:
                d += 1
        
        while r > 0 and d > 0:
            r -= 1
            d -= 1
        
        return "Radiant" if r > 0 else "Dire"
    

        #Time Complexity: O(n)
        #Space Complexity: O(1)



        #Other Solutions:
        class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        queueR=deque()
        queueD=deque()
        n=len(senate)
        for i,char in enumerate(senate):
            if char=='R':
                queueR.append(i)
            else:
                queueD.append(i)

        while queueR and queueD:
            r,d=queueR.popleft(),queueD.popleft()
            if r<d:
                queueR.append(r+n)
            else:
                queueD.append(d+n)

        return "Dire" if queueD else "Radiant"
    

    #Time Complexity: O(n)
    #Space Complexity: O(n)
# 1. The time complexity is O(n) because we are iterating through the list of senators once to build the queues and then processing the queues until one of them is empty.
# 2. The space complexity is O(n) because we are using two queues to store the indices of the senators from each party. In the worst case, all senators could be from one party and stored in the queue.
