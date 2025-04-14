n,n1,n2=map(int, input().split())
arr=list(map(int, input().split()))
arr.sort(reverse=True)
n1Val=0
n2Val=0
res=0
if n1>n2:
    n1,n2=n2,n1
for i in range((n1+n2)):
    if i<n1:
        n1Val+=arr[i]
    else:
        n2Val+=arr[i]
n1Val=n1Val/n1
n2Val=n2Val/n2
res=format((n1Val+n2Val),'.8f')
print(res)