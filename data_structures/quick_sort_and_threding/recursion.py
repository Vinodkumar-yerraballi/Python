def sum_of_eleements(n):
    sum =0
    for i in range(1,n+1):
        sum +=i
    return sum

#Another method to find the sum
def find_sum(n):
    if n==1:
        return 1
    return n+find_sum(n-1)
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)
if __name__=="__main__":
    print(sum_of_eleements(24))
    print(find_sum(5))
    print(fib(6))