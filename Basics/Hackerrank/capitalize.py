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


<<<<<<< HEAD
# reverse the list of numbers
numbers=[1,3,8,4,83]
def reverse_list(get_list):
    for i in range(len(get_list)):
        for j in range(len(get_list)+1):
            while (i>j):
                i+=1
                j-=1
print(reverse_list(numbers))
=======
string_1 = "Camelot"
string_2 = "place"

print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

name = "Alex"
quest = "Teaching Python"
color = "Blue"

print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))
>>>>>>> 6ca7c498896dc45fd098e544289994e00a073717
