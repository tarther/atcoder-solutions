import string

s=input()
lowercase_list = list(string.ascii_lowercase)

for str in s:
    if str in lowercase_list:
        lowercase_list.remove(str)

for i in lowercase_list:
    print(i)
    exit()