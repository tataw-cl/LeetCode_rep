# 690. Employee Importance
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

# You are given an array of employees employees where:

# employees[i].id is the ID of the ith employee.
# employees[i].importance is the importance value of the ith employee.
# employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.
# Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.

 

# Example 1:


# Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
# Output: 11
# Explanation: Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3.
# They both have an importance value of 3.
# Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.
# Example 2:


# Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
# Output: -3
# Explanation: Employee 5 has an importance value of -3 and has no direct subordinates.
# Thus, the total importance value of employee 5 is -3.
 

# Constraints:

# 1 <= employees.length <= 2000
# 1 <= employees[i].id <= 2000
# All employees[i].id are unique.
# -100 <= employees[i].importance <= 100
# One employee has at most one direct leader and may have several subordinates.
# The IDs in employees[i].subordinates are valid IDs.


#My Solution:class Employee:
"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        employeeMap={}
        for employee in employees:
            employeeMap[employee.id]=employee
        
        def dfs(emp):
            res = emp.importance
            for subordinate in emp.subordinates:
                res += dfs(employeeMap[subordinate])
            
            return res

        return dfs(employeeMap[id])
    

#Time Complexity: O(n), where n is the number of employees.
# Space Complexity: O(n), where n is the number of employees, due to the recursion stack and the employee map.


#Other Solution:
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        employeeMap = {employee.id: employee for employee in employees}
        
        def dfs(emp_id):
            emp = employeeMap[emp_id]
            total_importance = emp.importance
            for sub_id in emp.subordinates:
                total_importance += dfs(sub_id)
            return total_importance
        
        return dfs(id)
    
# Time Complexity: O(n), where n is the number of employees.
# Space Complexity: O(n), where n is the number of employees, due to the recursion
