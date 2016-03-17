import functools
import random

#
# listNums = [1, 3, 4, 5]
# sumSquare = functools.reduce(lambda a, y: a + y, map(lambda x: x * x, listNums))
# print(sumSquare)
#
# listStrings = ["Count how many time a \"n\" occurs in text",
#                "This is another sentence, may be a has better frequence than n ?"];
#
#
# def fact(n):
#     p = 1
#     for i in range(2, n + 1):
#         p *= i
#     return p
#
#
# def funFact(n):
#     return functools.reduce(lambda p, x: p * x, range(1, n + 1), 1)
#
#
# def count(s: str, c):
#     return functools.reduce(lambda a, cc: a + (1 if cc.upper() == c.upper() else 0), s, 0)
#
#
# assert fact(5) == funFact(5)
#
#
# def countCharInList(list, c):
#     # return functools.reduce(lambda a, x: a + x, map(lambda s: count(s, c), list))
#     return functools.reduce(lambda a, s: a + s.count(c), list, 0)
#
#
# print(listStrings)
# print("A occurs: ", countCharInList(listStrings, 'a'))
# print("N occurs: ", countCharInList(listStrings, 'n'))



# names = ["Son", "Long", "Duc"]
# codes = [1, 3, 5]
#
# # Return a map: name -> code
# encodedNames = dict(map(lambda name: (name, random.choice(codes)), names))
#
# for name in encodedNames.keys():
#     print(name + " = ", encodedNames[name])
# print("NAME = ", name)
#
# print(encodedNames)

# people = [{'name': 'Sam'}]

# people = [{'name': 'Mary', 'height': 160},
#           {'name': 'Isla', 'height': 80},
#           {'name': 'Sam'}]
#
# heights = list(map(lambda  p: p.get('height'), filter(lambda p: p.get('height', -1) != -1, people)))
# if len(heights) > 0:
#     avg = 1.0 * functools.reduce(lambda s, x: s+x, heights) / len(heights)
# print("Avg height = ", avg)


# Experiment: call by reference ?