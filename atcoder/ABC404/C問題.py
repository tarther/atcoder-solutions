import sys
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
g=[[] for _ in range(n+1)]
jisuu=[0]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
    jisuu[a]+=1
    jisuu[b]+=1

vis=[False]*(n+1)

def dfs(x):
    vis[x]=True
    for i in g[x]:
        if not vis[i]:
            dfs(i)

dfs(1)
for i in range(1, n+1):
    if not vis[i]:
        print("No")
        exit()

for i in range(1, n+1):
    if jisuu[i]!=2:
        print("No")
        exit()

print("Yes")