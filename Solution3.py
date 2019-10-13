def nodec(l):
    x=-1
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            if x!=-1:
                return False
            x=i
    return (x==0 or x==-1  or x==len(l)-2 or l[x-1]<=l[x+1] or l[x]<=l[x+2])
l=eval(input())
print(nodec(l))
