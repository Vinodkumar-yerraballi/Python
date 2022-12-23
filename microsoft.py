def add_two_sum(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[j]==target-num[i]:
                return [i,j]
            
number=[1,5,8,7]
print(add_two_sum(number,12))

# another method
def add_sum(num,target):
    # 
    for i in range(len(num)):
        for j in range(i+2,len(num)):
            if num[j]==target-num[i]:
                return [i,j]
            
print(add_sum(number,12))

def add_to_numbers(num,target):
    a={}
    for i in range(len(num)):
        diff=target-num[i]
        if diff in a:
            return [i,a[diff]]
        a[num[i]]=i
print(add_to_numbers(number,12))
a=[1,2,3,4,5]
sum=0
for ele in a:
    sum +=ele
print(sum)
def revers(s):
    s1=''
    for c in s:
        s1=c+s1
    return s1
apple='hello world'
print(revers(apple))

    


            
