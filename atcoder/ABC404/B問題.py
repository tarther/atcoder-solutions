n=int(input())
s=[input() for _ in range(n)]
t=[input() for _ in range(n)]

ans=10**10

cnt=0
for i in range(n):
    for j in range(n):
        if s[i][j]!=t[i][j]:
            cnt+=1
ans=min(ans,cnt)

s2=[[] for _ in range(n)]
for i in range(n):
    for j in range(n-1, -1 ,-1):
        s2[i].append(s[j][i])

cnt=0
for i in range(n):
    for j in range(n):
        if s2[i][j]!=t[i][j]:
            cnt+=1
ans=min(ans,cnt+1)

s3=[[] for _ in range(n)]
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        s3[n-1-i].append(s[i][j])

cnt=0
for i in range(n):
    for j in range(n):
        if s3[i][j]!=t[i][j]:
            cnt+=1
ans=min(ans,cnt+2)

s4=[[] for _ in range(n)]
for i in range(n-1, -1, -1):
    for j in range(n):
        s4[n-1-i].append(s[j][i])

cnt=0
for i in range(n):
    for j in range(n):
        if s4[i][j]!=t[i][j]:
            cnt+=1
ans=min(ans,cnt+3)

print(ans)