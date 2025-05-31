import math
t=int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1 or n == 2:
        print(-1)
        continue
    else:
        total = sum(a)
        a.sort()
        #min discontent threshold is 2 * n * a[i] - total
        res = -1  # Default result if no valid threshold is found
        # Try each threshold starting from smallest ai
        discontent_thresholds = [((2 * n * ai) - total)+1 for ai in a]

        mid= n // 2
        if discontent_thresholds[mid+1] > -1:
            res=discontent_thresholds[mid+1]
        # Goal: find minimum x such that discontent > n // 2
        # for i in range(n):
        #     required_x = discontent_thresholds[i]
        #     count_discontentPeople = i + 1  # since a is sorted, these are all < threshold
        #     if required_x > -1 and count_discontentPeople > n // 2:
        #         res=required_x
        #         break

    print(res)
