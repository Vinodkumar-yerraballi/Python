list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row, col = 3, 3
for i in range(row+col-1):
    result = []
    for j in range(row):
        for k in range(col):
            if (i == j+k):
                result.append(list1[j][k])
    print(*result)
print('-----------------------------------------------')
print('-----------------------------------------------')
a = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
row1, col1 = 3, 3
for i in range(row1+col1-1):
    result_1 = []
    for j in range(row1):
        for k in range(col1):
            if (i == j+k):
                result_1.append(a[j][k])
    print(*result_1)
