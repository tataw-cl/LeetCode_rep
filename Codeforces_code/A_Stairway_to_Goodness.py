t=int(input())
for _ in range(t):
    l,r=map(int, input().split())
    diff=1
    num=l
    count=0
    while num<=r:
        num+=diff
        diff+=1
        count+=1

    print(count)
