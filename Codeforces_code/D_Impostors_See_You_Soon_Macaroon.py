t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    res=0
    if 'W' not in s:
        res= max(0, 2 * k - 1 if k > 0 else 0)

    score = 0
    gaps = []
    i = 0

    # Count initial score & collect gaps between W streaks
    while i < n:
        if s[i] == 'W':
            score += 1
            if i > 0 and s[i - 1] == 'W':
                score += 1
            i += 1
        else:
            j = i
            while j < n and s[j] == 'L':
                j += 1
            if i != 0 and j != n:  # only count inner gaps
                gaps.append(j - i)
            i = j

    # Fill the smallest gaps first
    gaps.sort()
    for gap in gaps:
        if k >= gap:
            score += gap * 2 + 1  # flip all Ls and connect streaks
            k -= gap
        else:
            score += k * 2
            k = 0
            break

    # Use remaining k on edge Ls
    score += k * 2

    print (min(score, 2 * n - 1))  # Max score is 2*(n)-1
