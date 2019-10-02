s=list(map(str,input().split()))
k=int(input(""))
p=[]
o=""
o=o+s[0]
for i in s[1::]:
    f=o
    o=o+" "+ i
    if len(o)>k:
        p.append(f)
        o=""
        o=i
if k < len(i):
    print("null")
else:
    p.append(o)
    print(p)
