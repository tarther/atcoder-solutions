from collections import deque

Q=int(input())

t=deque()

for i in range(Q):
    q=list(map(int,input().split()))
    if q[0]==1:
        t.append(q[1])
    elif q[0]==2:
        x=t.popleft()
        print(x)