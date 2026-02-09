n,m,Q=map(int,input().split())

user=[set() for _ in range(n+1)]

for i in range(Q):
    q=list(map(int,input().split()))
    if q[0]==1:
        user[q[1]].add(q[2])
    elif q[0]==2:
        user[q[1]].add(10**10)
    else:
        if q[2] in user[q[1]] or 10**10 in user[q[1]]:
            print("Yes")
        else:
            print("No")