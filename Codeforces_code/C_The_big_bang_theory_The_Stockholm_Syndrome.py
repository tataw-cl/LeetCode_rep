n=int(input())
arr=list(map(int, input().split()))
arr.sort()

res=1
for val in arr:
    if val>=res:
        res+=1
print(res)
