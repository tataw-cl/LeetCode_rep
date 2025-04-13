t=int(input())
for _ in range(t):
    ways=0
    n,k,q=map(int, input().split())
    arr=list(map(int, input().split()))

    count = 0
    length = 0

    for i in range(n):
        if arr[i] <= q:
            length += 1
        else:
            if length >= k:
                valid = length - k + 1
                count += valid * (valid + 1) // 2
            length = 0

    
    if length >= k:
        valid = length - k + 1
        count += valid * (valid + 1) // 2
    print(count)



    # conseqDays=[]
    # count=0
    # for i in range(n):
    #     if arr[i]<=q:
    #         count+=1
    #     else:
    #         conseqDays.append(count)
    #         count=0
    # print(conseqDays)
    # for elem in conseqDays:
    #     if elem >=k:
    #         ways+=((elem-k+1)*(elem-k+2))//2
    # print(conseqDays)