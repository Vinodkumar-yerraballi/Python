n=int(input())
j=0
k=2*n-1
for i in range(1,n+1):
    left_space="  "*(j)
    k=k-2
    j=j+2
    print(left_space+"* "*k)
for i in range(n):
    spaces="    " *(i)
    stars="* "*((2*(n-i))-1)
    print(spaces+" "+stars)