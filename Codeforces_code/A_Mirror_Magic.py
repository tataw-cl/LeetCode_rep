t=input()
mapping = {'q': 'p','p': 'q', 'w': 'w'}
for _ in range(int(t)):
    a = input()
    b=[]
    for i in range(len(a)-1, -1, -1):
            b.append(mapping[a[i]])
    print("".join(b))
