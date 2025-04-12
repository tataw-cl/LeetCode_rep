n=int(input())
arr=list(map(int,input().split()))

hasOdd=any(x%2==1 for x in arr)
hasEven=any(x%2==0 for x in arr)
if hasOdd and hasEven:
    arr.sort()
print(*arr)