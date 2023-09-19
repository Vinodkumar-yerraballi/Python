s=input()
shuffle_s= ""

for i in range(len(s)):
    index_shuffle= int(input())
    shuffle_s=shuffle_s + s [index_shuffle]
    print(shuffle_s)
print(shuffle_s)


# find the prime number

prime=input()
factor=0

for i in range(2,prime):
    if (prime % i == 0):
        factor=factor+1
if factor==0:
    print("Prime number")
else:
    print("Not a Prime number")

