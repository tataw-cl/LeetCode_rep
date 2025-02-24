import sys
Data=sys.stdin.read().strip().splitlines()
n,m=map(int, (Data[0].split()))
mat=[['#' for _ in range(m)]for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i%2==1:
            mat[i][j]="."
            if (i//2)%2==0:
                mat[i][m-1]='#'
            else:
                mat[i][0]="#"
for row in mat:
    print(''.join(row))