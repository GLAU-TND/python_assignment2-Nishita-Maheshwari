a=list(map(int,input().split(',')))
k=int(input())
b=[]

for i in range(len(a)-2):
    if(a[i]+a[i+1]+a[i+2]==k):
        b.append([a[i],a[i+1],a[i+2]])
    
if(b==[]):
    print(None)
else:
    print(*b)
        

