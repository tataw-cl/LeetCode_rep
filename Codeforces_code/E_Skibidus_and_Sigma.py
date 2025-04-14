t=int(input())
for _ in range(t):
    n,m=map(int, input().split())
    arr=[]
    res=[]
    for i in range(n):
        arr.append(list(map(int, input().split())))
    sumArr=[(sum(row), row) for row in arr]
    sumArr.sort(reverse=True, key=lambda x: x[0])
    for _,row in sumArr:
        res.extend(row)
    score=0
    preSum=0
    for val in res:
        preSum+=val
        score+=preSum
    print(score)
