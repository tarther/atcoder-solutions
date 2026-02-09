t=input()
u=input()

for i in range(len(t)-len(u)+1):
    cnt=0
    for j in range(len(u)):
        if t[i+j]==u[j] or t[i+j]=="?":
            continue
        else:
            break
    else:
        print("Yes")
        exit()

print("No")