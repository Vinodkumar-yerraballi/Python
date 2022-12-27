def buble_sort(elements):
    size=len(elements)
    for i in range(size-1):
        swapped=True
        for j in range(size-1-i):
            if elements[j]>elements[j+1]:
                temp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=temp
                swapped=False
        if not swapped:
           break
    
if __name__=="__main__":
    number=[1,4,2,44,65,99]
    buble_sort(number)
    print(number)

        