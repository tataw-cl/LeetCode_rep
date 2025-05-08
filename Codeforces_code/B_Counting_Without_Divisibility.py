t=int(input())
for _ in range(t):
    n,k=map(int, input().split())
    m=n-1
    res=-1
    while m<k:
        m+=m
    diff=m-k
    nOcc=(m//n)+1
    res=(m-diff)+nOcc
    print(res)