# Let's create a supermarket system with opps methods and attributes are called items and methods are actions


# let's define the supermarket class

class Supermarket:
    def __init__(self,grocary,friuts,jucises,cloths,washingitems):
        self.grocary = grocary
        self.friuts =friuts
        self.jucises = jucises
        self.cloths = cloths
        self.wasingitems =washingitems

    # actions
    def purchase_items(self,age):
        if age >10:
            print("Purchase the items")
            
        else:
            print('not allowed to purchase')
        return
supermarket=Supermarket("pennets","apple","mango jucises","shirts","detergentpoweder")
print(supermarket.purchase_items(5))