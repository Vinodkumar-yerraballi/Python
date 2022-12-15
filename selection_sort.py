def selection_sort(arr):
    size=len(arr)
    for i in range(size-1):
        mid_index=i
        for j in range(mid_index+1,size):
            if arr[j] < arr[mid_index]:
                mid_index=j
        if i!=mid_index:
            arr[i],arr[mid_index]=arr[mid_index],arr[i]

if __name__=='__main__':
    elemenets=[2,1,3,4,5,6,7,9]
    selection_sort(elemenets)
    print(elemenets)
    test=[
        [88,8,0,1,2,99,1999,686,3974],
        [1,2,3,4,5,6],
        [],
        
    ]
    for element in test:
        selection_sort(element)
        print(element)


