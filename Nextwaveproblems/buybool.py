'''if the book is equal to large  and pagers greter then and equal to 300 
returns to buy a book otherwise returns do not buy a book
'''

# we take the book information from the user
book=input()
# pages
page=int(input())
# condition
condition=(book=='large' or page>=300)
if condition:
    print('Buy a book')
else:
    print('Not buy a book')