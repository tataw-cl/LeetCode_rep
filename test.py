s = "abcabc"
l,r=0,len(s)-1
seen=set()
res=0
while l<r:
    while l<r:
        seen.clear()
        for i in range(l,r+1):
            seen.add(s[i])
            if len(seen)==3:
                res+=1
                break
        r-=1
    l+=1
        
print(res)