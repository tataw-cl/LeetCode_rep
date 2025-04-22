from collections import Counter
n=int(input())
word=input()
wordCount=Counter(word)
zeros=wordCount['z']
ones=wordCount['n']
ans=""
if ones> 0:
    for _ in range(ones):
        ans+="1 "
if zeros>0:
    for _ in range(zeros):
        ans+="0 "

print(ans)
# The code takes an integer n and a string word as input. It counts the occurrences of 'z' and 'n' 
# in the string using the Counter class from the collections module.
# Then, it constructs a new string ans based on the counts of 'z' and 'n', appending '1' for
# each occurrence of 'n' and '0' for each occurrence of 'z'.Finally, it prints the constructed string
# without trailing spaces.
