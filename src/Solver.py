import math


class Solver:
    def demo(self):
        a = int(input("a "))
        b = int(input("b "))
        c = int(input("c "))
        d = b ** 2 - 4 * a * c
        disc = math.sqrt(d)
        root1 = (-b + disc) / (2 * a)
        root2 = (-b - disc) / (2 * a)
        print(root1, root2)


def pythagoras(a, b) -> float:
    """

    :rtype: float
    """
    value = a ** 2 + b ** 2
    return math.sqrt(value)


# x = int(input("X = "))
# if x == 4:
#     print("Right")
# else:
#     print("Wrong")
# print("Done")

y = 4
print(y)
y = 4.5
print(y)
#
# for i in range(1, 10):
#     print(i)

print("pyta", pythagoras(3, 4))
c = [5,2,10,48,32,16,49,10,11,32,64,55,34,45,41,23,26,27,72,18]
print("Len: ", len(c))
# for i in range(0,len(c)):
#     print("c[",i,"]= ", c[i])

m = {"MALE": 80, "FEMALE": 20}
for key in m.keys():
    print(key, "= ", m[key])