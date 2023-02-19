def power(base,exponement):
    print('{} to the power{}={}'.format(base,exponement,base**exponement))
    return base**exponement

def square(base):
    return power(base,2)

def cube(base):
    return power(base,3)

print(square(2))
print(cube(3))

def outerfunction(text):
    text=text
    def innerfunction():
        print(text)
    return innerfunction

print(outerfunction("Hey hi welcome to my home"))