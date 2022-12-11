import math
import os
import random
import re
import sys


# write your code here
def avg(*num):
    if len(num)==0:
        return None
    sum=0
    for i in num:
        sum=sum+i
        moy=sum/len(num)
    return(moy)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = map(int, raw_input().split())
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
