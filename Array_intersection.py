from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        # Count the occurrences of each number in both lists
        count_nums1 = Counter(nums1)
        count_nums2 = Counter(nums2)
        
        # Find the intersection by getting the minimum occurrences of each element in both lists
        intersection = count_nums1 & count_nums2
        
        # Convert the intersection to a list, considering the number of occurrences
        result = []
        for num in intersection.elements():
            result.append(num)
        
        return result