t=int(input())
for _ in range(t):
    n,m =map(int, input().split())
    arr=list(map(int, input().split()))
    if n>m:
        print("NO")
        continue
    check=0
    arr.sort(reverse=True)
    check+=arr[0]
    for i in range(n):
        if i != n-1:
            check+=(arr[i] + 1)
        else:
            check+=1

    if check>m:
        print("NO")
        continue
    else:
        print("YES")
        continue
    