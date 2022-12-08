def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find: # this means number is in right hand side of the list
            left_index = mid_index + 1
        else: # number to find is on left hand side of the list
            right_index = mid_index - 1

    return -1
def find_all_accurance(number_list,number_to_find):
    index=binary_search(numbers_list, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if number_list[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(number_list):
        if number_list[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)
    

if __name__=="__main__":
    # numbers_list=[1,4,6,9,10,5,7]
    # number_to_find=5
    # index=binary_search(numbers_list, number_to_find)
    # print(f'the bineary search {index}')
    numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 1
    indices = find_all_accurance(numbers_list, number_to_find)
    print(f"Indices of occurances of {number_to_find} are {indices}")


