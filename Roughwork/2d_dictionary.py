# Create a 2d dictionary 


dict_items={
    'RCB':{
        'batman':'virat',
        'captain':'faf',
        'bowler':'siraj'

    },
    'CSK':{
        'batman':'Ruthuraj',
        'captain':'MSD',
        'bowler':'jaddu'
    }
}

print(dict_items.keys())
print(dict_items.values())


# Count the frequency of elements in the list

input_list=[1,1,2,3,4,5,5,6,7]

# create a fucntion to  find the frequency of elements

def find_frequency(input_list):
    # create a dictionary
    ouput={}
    # iterate over  the input list
    for i in input_list:
        ouput[i] = ouput.get(i,0)+1
        print(i,ouput[i])
    return ouput 

print(find_frequency(input_list))