n=int(input())
a=list(map(int,input().split()))
l,r=0,len(a)-1
player1=0
player2=0
round=0
while l<=r:
    if round%2==0:
        if a[l]>a[r]:
            player1+=a[l]
            l+=1
        else:
            player1+=a[r]
            r-=1
    else:
        if a[l]>a[r]:
            player2+=a[l]
            l+=1
        else:
            player2+=a[r]
            r-=1
    round+=1

print(player1,player2)

