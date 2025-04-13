n=int(input())
arr=list(map(int, input().split()))
arr.sort()
res=[]
state=True
x=0
j=n-1
for i in range(n):
    if i%2==0:
        res.append(arr[x])
        x+=1
    else:
        res.append(arr[j])
        j-=1

for i in range(n):
    if i%2==0:
        if res[i-1]>=res[i]:
           continue
        else:
            state=False
            break
    elif i%2!=0:
        if res[i-1]<=res[i]:
            continue       
        
        else:
            state=False
            break
    
if state:
    print(*res)
else:
    print("Impossible")
