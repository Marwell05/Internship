user=input("Enter a string ")
d1=dict()
for st in user:
    if (st in d1):
        d1[st]=d1[st]+1
    else:
        d1[st]=1
print(d1)