def buble_sort(elements,key=None):
    size=len(elements)
    for i in range(size-1):
        swapped=True
        for j in range(size-1-i):
            a= elements[i][key]
            b=elements[j+1][key]
            if a > b:
                temp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=temp
                swapped=False
        if not swapped:
            break


# Anothe method
def buble_sort(elements,key=None):
    size=len(elements)
    for i in range(size-1):
        swapped=False
        for j in range(size-1-i):
            if elements[i][key] > elements[j+1][key]:
                temp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=temp
                swapped=True
        if not swapped:
            break
if __name__=="__main__":
    elements = [
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]
    buble_sort(elements,key='name')
    print(elements)