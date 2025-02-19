# HackerLand University has the following grading policy: 
#  Every student receives a  in the inclusive range from  to .
# Any  less than  is a failing grade.
# Sam is a professor at the university and likes to round each student's  according to these rules: 
#  If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
# If the value of  is less than , no rounding occurs as the result will still be a failing grade.
# Examples 
#  round to  (85 - 84 is less than 3)
# do not round (result is less than 38)
# do not round (60 - 57 is 3 or higher)
# Given the initial value of  for each of Sam's  students, write code to automate the rounding process. 
#  Function Description 
#  Complete the function  with the following parameter(s): 
#  : the grades before rounding
# Returns 
#  : the grades after rounding
# Input Format 
#  The first line contains a single integer, , the number of students.
# Each line  of the  subsequent lines contains a single integer, . 
#  Constraints 

#My Solution:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] >=38:
            next_Multiple_Of_5=(((grades[i]//5)+1)*5)
            if (next_Multiple_Of_5-grades[i])<3:
                grades[i]=next_Multiple_Of_5
    return grades
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

    #Time Complexity: O(n)
    #Space Complexity: O(1)

#Other Solution:
def gradingStudents(grades):
    return [grade if grade < 38 or grade % 5 < 3 else grade + 5 - grade % 5 for grade in grades]

    #Time Complexity: O(n)
    #Space Complexity: O(1)