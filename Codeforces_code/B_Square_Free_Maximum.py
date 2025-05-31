import math

def is_perfect_square(x):
    if x < 0:
        return False
    root = int(math.isqrt(x))
    return root * root == x

n = int(input())
arr = list(map(int, input().split()))

max_non_square = -10**9

for x in arr:
    if not is_perfect_square(x):
        max_non_square = max(max_non_square, x)

print(max_non_square)
