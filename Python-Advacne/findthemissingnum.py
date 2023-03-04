#Define the function to find the missing numbers
def Findthemissingnum(n):
    number=set(n)
    length=len(n)
    result=[]
    for i in range(1,n[-1]):
        if i not in number:
            result.append(i)
    return result

#Another method to solve te missinnumbes
def missing_number(nums):
  n=len(nums)
  expected_sum = int(n*(n+1)/2)
  actual_sum = sum(nums)
  missing = expected_sum - actual_sum
  return missing






numbers=[1,2,4,6,8,9]
num1=[0,2,4,6]
result=Findthemissingnum(numbers)
result_1=missing_number(num1)
print("Missing numbers in the array is",result)
print("Missing numbers in the array is",result_1)