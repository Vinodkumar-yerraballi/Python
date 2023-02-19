fruits=['apple','banna','cherray','mango']
new_fruits=[]
for i in fruits:
    if 'a' in i:
        new_fruits.append(i)
print(new_fruits)
#anothe way to write same method
new_fruit=[new for new in fruits if 'a' in new]
print(new_fruit)

human=[]
for letters in 'human':
    human.append(letters)
print(human)
#another method for it
new_human=[letter for letter in 'human']
print(new_human)

new_list=[x for x in range(20) if x%2==0]
print(new_list)
new_squar=[x for x in range(20) if x*2]
print(new_squar)
new_list1=[y for y in range(20) if y%2==0 and y%5==0]
print(new_list1)

obj=['Even' if i%2==0 else 'Odd' for i in range(10)]
print(obj)

def double(x):
    return x*2
new_list2=[double(x) for x in range(10)]
print(new_list2)
text='We look at the earth and see the how the moon is beautiful'
new_text={vowels for vowels in text if vowels in 'aeiou'}
print(new_text)
square={i:i*2 for i in range(10)}
print(square)
