def catpitalize_the_name(name):
    output=name.title()
    return output

def captilize(name):
    return ' '.join(word.capitalize() for word in name.split(' '))
value="VINOD KUMAR"
print(catpitalize_the_name(value))
print(captilize(value))

def find_the_number(number,list_a):
    for i in range(len(list_a)):
        print(i)
        # if number==list_a[i]:
        #     return i
list_b=[1,3,8,4,83]
number=3
print(find_the_number(number,list_b))