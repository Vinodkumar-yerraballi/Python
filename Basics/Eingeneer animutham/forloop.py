a=[1,2,3,1,4,5,1,1,1,6]
ans=0
for i in a:
    if i==1:
        ans+=1
print(ans)

b=[1,2,3,4,5,6,7,1,1,1,1,2,2,3,3,4]
out=0
for i in b:
    if b[i]==1:
        out+=1
print(out)
for i in range(1,10+1,2):
    print(i)
    
a=[1,2,3,4,5]
for i in range(len(a)):
    print(a[i])
    
b=[1,2,1,3,1,4,1,5,1,6,1,1,2,2]
ans=0
for i in range(len(b)):
    if b[i]==1 or b[i]==2:
        ans=ans+1
print(ans)