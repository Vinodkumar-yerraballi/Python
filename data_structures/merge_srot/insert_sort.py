def insert_sort(elements):
    for i in range(1,len(elements)):
        anchor=elements[i]
        j=i-1
        while j >=0 and anchor  <  elements[j]:
            elements [j+1]=elements[j]
            j=j-1
            elements[j+1]=anchor

if __name__=="__main__":
    test=[1,3,5,6,2,9]
    insert_sort(test)
    print(test)

def place_to_insert(array, key):
    index = 0
    for i in array:
        if i > key:
            break
        else:
            index += 1
    return index


def insert_to_sorted(array, key):
    index = place_to_insert(array, key)
    return array[0:index]+[key]+array[index:]


if __name__ == "__main__":
    array = [2, 1, 5, 7, 2, 0, 5]

    stream = []

    count = 0
    while(True):
        i = int(input())
        count += 1
        stream = insert_to_sorted(stream, i)
        if count % 2 == 1:
            print(f"Median of {stream} : {stream[(count)//2]}")
        else:
            i1 = count//2
            i2 = (count//2) - 1
            print(f"Median of {stream} : {(stream[i1] + stream[i2])/2}")