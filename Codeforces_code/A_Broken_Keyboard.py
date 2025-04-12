t=int(input())
for _ in range(t):
    res=""
    s=input()
    n=len(s)
    if n==1:
        print(s)
        continue
    else:
        for r in range(n):
                if r==0:
                    if s[r]!=s[r+1]:
                        res+=s[r]
                elif r==n-1:
                    if s[r]!=s[r-1]:
                        res+=s[r]
                else:
                    if s[r-1]!=s[r] and s[r]!=s[r+1]:
                        res+=s[r]
    res="".join(sorted(res))
    print(res)