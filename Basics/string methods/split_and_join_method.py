# Split the string 

# when create a new list with space it takes default as whitespace
# example: list
list_a='1 2 3 4 5 6 7 8 9'
new_list_a = list_a.split()
print(new_list_a)   # output ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# if you give the space between the two numvers its default takes the whitespace 

# Second example
list_b='1 234'
new_list_b=list_b.split()
print(new_list_b) # output ['1', '234']

# we can also split the string also with words and letter also

sentence="Python is best programming language"
split_sentence=sentence.split('a')
print(split_sentence) # output ['Python is best progr', 'mming l', 'ngu', 'ge']

sentence_split_word=sentence.split('is')
print(sentence_split_word) # output ['Python ', ' best programming language']

################################################################

# Join method in the string
another_sentence="Power people make place powerful"
# we split the stence with  letter a in above sentence
after_sentence=another_sentence.split('a')
print(after_sentence) # output ['Power people m', 'ke pl', 'ce powerful']

new_sentence_after_split_word='a'.join(after_sentence) 
print(new_sentence_after_split_word)# output   Power people make place powerful

# if add the numbers using join method we get error
numbers=list(range(4))
join_numbers=','.join(numbers) 
print(join_numbers) # output  TypeError: sequence item 0: expected str instance, int found