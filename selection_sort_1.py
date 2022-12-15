def multi_sort_elements(elements,sort_by_list):
    for sort_by in sort_by_list[-1::-1]:
        for x in range(len(elements)):
            mid_index=x
            for y in range(x,len(elements)):
                if elements[y][sort_by]<elements[mid_index][sort_by]:
                    mid_index=y
            if x!=mid_index:
                elements[x],elements[mid_index]=elements[mid_index],elements[x]








if __name__=="__main__":
    test=[
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]
    print(f'Given unsorted array:', *test, sep='\n')
    multi_sort_elements(
        test, ['First Name', 'Last Name'])
    print(f'Array after Multi-Level Sorting:', *test, sep='\n')
