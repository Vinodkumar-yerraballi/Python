from util import time_it
@time_it
def linear_search(number_list,number_find_it):
    for index,element in enumerate(number_list):
        if element == number_find_it:
            return  index
    return -1
#bineary search
@time_it
def binear_search(number_list,number_find_it):
    left_index=0
    right_index=len(number_list)-1
    midel_index=0
    while left_index<=right_index:
        midel_index=(left_index+right_index)//2
        mid_number=number_list[midel_index]
        if mid_number==number_find_it:
            return midel_index
        if mid_number<number_find_it:
            left_index =midel_index +1
        else:
            right_index = midel_index -1
    return -1
@time_it
def bineary_search_recersive(number_list,number_find_it,left_index,right_index):
    if right_index<left_index:
       return -1
    mid_index=(left_index+right_index)//2
    if mid_index >=len(number_list) or mid_index < 0:
        return -1
    mid_number=number_list[mid_index]
    if mid_number==number_find_it:
        return mid_index
    if mid_number< number_find_it:
        left_index=mid_index +1
    else:
        right_index = mid_index-1

    return bineary_search_recersive(number_list,number_find_it,left_index,right_index)


if __name__ == "__main__":
    number_list=[i for i in range(1,100)]
    number_find_it=33
    index=linear_search(number_list,number_find_it)
    index1=binear_search(number_list,number_find_it)
    index2=bineary_search_recersive(number_list,number_find_it,0,len(number_list))
    print(f'find the linear seach for {index}')
    print(f'find the bineary_seach for {index1}')
    print(f'find the bineary_seach for {index2}')
    