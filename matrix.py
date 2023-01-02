import numpy as np
A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]


result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]
# result = np.dot(A, B)
for i in result:
    print(i)
A = [[1, 2, 3], [5, 3, 1], [7, 9, 8]]
B = [[3, 4], [12, 4], [8, 14]]

# retrieving the sizes/dimensions of the matrices
p = len(A)
q = len(A[0])
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j-1]+B[i][j-1]
for k in result:
    print(k)

name = 'abcdef'
name_1 = 'abc'


def substing(s):
    n = len(s)
    for i in range(n//2, 0, -1):
        if (n % i == 0):
            string = s[:i]
            times = n//i
            number = string*times
            if number == s:
                return True

    return False


class Human:
    name_human = None
    age_human = None

    def get_name(self):
        print("Enter name")
        self.name_human = input()

    def get_age(self):
        print("Enter your age")
        self.age_human = input()

    def put_name(self):
        print("Your name", self.name_human)

    def put_age(self):
        print('You age is', self.age_human)


human = Human()
# print(human.get_age())
human.get_name()


class fruit:
    def __init__(self):
        print("I'm the man")


class fruits(fruit):
    def __init__(self):
        super().__init__()
        print("I'm also human being")


man = fruits()
print(man)
