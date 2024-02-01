# n=int(input())
# input_users=map(int,input().split())
# print(input_users)
# tuples=tuple(input_users)
# print(hash(tuples))

# Problem
uni_code=[1,2,3]
profti=[10,20,30]
n=len(uni_code)
ans=0
max_value=0
for i in range(0,len(uni_code)):
    max_value=max(profti[i],max_value)
    for j in range(i+1,n):
        if (uni_code[i]==uni_code[j]):
            max_value=max(uni_code[j],max_value)
        else:
            i=j-1
            break
    ans+=max_value
print(ans)

# uni_code = [1, 2, 3]
# profit = [10, 20, 30]
# n = len(uni_code)
# ans = 0
# max_value = 0

# for i in range(0, len(uni_code)):
#     max_value = max(profit[i], max_value)
    
#     for j in range(i + 1, n):
#         if uni_code[i] == uni_code[j]:
#             max_value = max(profit[j], max_value)
#         else:
#             i = j - 1
#             break

#     ans += max_value

# print(ans)

