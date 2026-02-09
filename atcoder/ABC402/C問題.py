from collections import defaultdict

n,m=map(int,input().split())
ka=[list(map(int,input().split()[1:])) for i in range(m)]
b=list(map(int,input().split()))

a=[0]*(n+1)
for i in range(n):
    a[b[i]]=i+1

day=[0]*n
for li in ka:
    ans=0
    for x in li:
        x=a[x]
        ans=max(ans, x)
    day[ans-1]+=1

total=0
for i in range(n):
    total+=day[i]
    print(total)