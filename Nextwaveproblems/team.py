a=int(input())
b=int(input())

conditions=a>300 and b>300
sum=a+b<500

if conditions==True and sum:
    print('Can team up')
else:
    print('Cannot team up')