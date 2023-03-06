s=input()

for i in range(1,len(s)+1):
    print(s[:i])

#output like
# V
# Vi
# Vin
# Vino
# Vinod

s=input()
print(s[::-1])
#output
#doniV

#Another method 
s=input()
shuffled=""
for i in range(len(s)):
    index=int(input())
    shuffled=shuffled+s[index]
print(shuffled)