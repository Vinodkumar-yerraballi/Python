# addition in the matrix
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row, col = 3, 3
for i in range(row):
    result = []
    for j in range(col):
        add = list1[i][j]+list2[i][j]
        result.append(add)
    print(result)

print('----------------------------------------')
print('----------------------------------------')
print('----------------------------------------')
print('----------------------------------------')
# subtraction in the matrix
a = [[5, 8, 9], [9, 8, 7]]
b = [[4, 2, 6], [0, 4, 2]]
c, d = 2, 3
for i in range(c):
    subtraction = []
    for j in range(d):
        final = a[i][j] - b[i][j]
        subtraction.append(final)
    print(subtraction)

print('---------------------------------------')
print('----------------------------------------')
# multplication
list3 = [[4, 5, 6], [6, 1, 4]]
list4 = [[6, 8, 9], [0, 1, 2]]
row1, col1 = 2, 3
for i in range(row1):
    multiplication = []
    for j in range(col1):
        final_result = list3[i][j] * list4[i][j]
        multiplication.append(final_result)
    print(multiplication)

print('---------------------------------------')
print('----------------------------------------')
# transpose
list5 = [[5, 6, 1], [9, 4, 0], [4, 2, 1]]
# list6 = [[9, 1, 2], [4, 2, 1]]
row2, cols2 = 3, 3
for i in range(row2):
    result_1 = []
    for j in range(cols2):
        result_1.append(list5[i][j])
    print(result_1)


# Principal dignoal
print('---------------------------------------')
print('----------------------------------------')
list6 = [[9, 1, 2], [4, 2, 1], [5, 6, 1]]
row3, cols3 = 3, 3
result_2 = []
for i in range(row3):

    for j in range(cols3):
        if (i == j):
            result_2.append(list6[i][j])
print(result_2)


# Seconday dignoal
print('---------------------------------------')
print('----------------------------------------')
list7 = [[7, 3, 2], [9, 6, 4], [2, 7, 1]]
row4, cols4 = 3, 3
result_3 = []
for i in range(row4):

    for j in range(cols4):
        if (i+j == cols4-1):
            result_3.append(list7[i][j])
print(result_3)
