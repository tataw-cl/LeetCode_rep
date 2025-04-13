t=int(input())
for _ in range(t):
    n=int(input())
    seats=list(map(int, input().split()))
    state=True
    seen=set()
    for i in range(n):
            seen.add(seats[i])
            if i==0:
                continue
            else:
                if (seats[i]+1 not in seen) and (seats[i]-1 not in seen):
                    state=False
                    break
                else:
                    continue
    if state:
        print("YES")
    else:
        print("NO")