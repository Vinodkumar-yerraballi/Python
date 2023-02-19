import re
pattern='^a---s$'
test_string='abyss'
result=re.match(pattern,test_string)
if result:
    print('Search succesful')
else:
    print('Search unsuceesful')
text='We have three main items in the list'
result1=re.match(r"[abc]",text)
result2=re.search(r"[m*n]",text)
result3=re.search(r'--','acd')
result4=re.search(r'a{2,3}','aabdfff')
print(result1)
print(result2)
print(result3)
print(result4)