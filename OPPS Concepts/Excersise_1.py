'''
Let's create a online platform to purchase the different products available
in the store and we print the output 

'''

class OnilneShoping:
    def __init__(self,mobile,electronics,grocery,books):
        self.mobile=mobile
        self.electronics=electronics
        self.grocery=grocery
        self.books=books

    # i create a list of items available in the my store 
    mobile_brands=['oneplus','apple','vivo']
    electronics_brands=['apple','hp','dell']
    grocery=['sugar','cofee','salts','detergent']
    books=['']