# pylint: disable=C0103, C0114, C0116,C0115, R0903, C0304
import string

# The zip() function takes iterables (can be zero or more),
# aggregates them in a tuple, and returns it.


# -- ===== ZIP

languages = ["Java", "Python", "JavaScript"]
versions = [14, 3, 6]

list(zip(languages, versions))  # [('Java', 14), ('Python', 3), ('JavaScript', 6)]
set(zip(languages, versions))  # {('Java', 14), ('Python', 3), ('JavaScript', 6)}
tuple(zip(languages, versions))  # (('Java', 14), ('Python', 3), ('JavaScript', 6))

# stop at the end of the shortest iterable
l1 = [1, 2, 3, 4, 5]
l2 = ["Pierre", "Paul"]
list(zip(l1, l2))  # [(1, 'Pierre'), (2, 'Paul')]

# -- other example
mynum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
words = {"Paris", "Milan", "New-York"}
person = (" John", "Patrick", "Anna")
transport = {1: "car", 2: "plane", 3: "boat"}

combineItems = zip(mynum, words, person, transport.values())
for item in combineItems:  # item is a tuple
    print(item)
# (1, 'Paris', ' John', 'car')
# (2, 'Milan', 'Patrick', 'plane')
# (3, 'New-York', 'Anna', 'boat')


# --------  ZIP pour créer une liste de tuples à partir de 2 listes
alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
indices = range(1, len(alphabet) + 1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, ... 26]
liste_zip = zip(indices, alphabet)  # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), ...
resultat = dict(liste_zip)  # {1: 'a', 2: 'b', 3: 'c', 4: 'd',

# -------- filter
# filter(function, sequence)
# filters the given sequence with the help of a function
# that tests each element in the sequence to be true or not.

sequence = ["g", "é", "e", "9", "k", "s", "p", "r"]
filtered = filter(lambda x: x in string.ascii_letters, sequence)
for item in filtered:
    print(item)

# -------- map
# Returns a list of the results after applying the given function
# to each item of a given iterable (list, tuple etc.)
# map(func, iter)

# -- example 1, with a lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))


# Define a function that doubles even numbers and leaves odd numbers as is
def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num


# Create a list of numbers to apply the function to
numbers = [1, 2, 3, 4, 5]

# Use map to apply the function to each element in the list
result = list(map(double_even, numbers))

# Print the result
print(result)  # [1, 4, 3, 8, 5]


# -------- yield


# -- example 1
def fun_generator():
    yield "Hello world!!"
    yield "Geeksforgeeks"


obj = fun_generator()
print(type(obj))
print(next(obj))
print(next(obj))


# output
# <class 'generator'>
# Hello world!!
# Geeksforgeeks


# -- example 2
def nextSquare():
    i = 1

    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes from this point


# Driver code to test above generator
# function
for num in nextSquare():
    if num > 100:
        break
    print(num)


# -- example 3
# func to count number of given word
def print_even(test_string):
    for i in test_string:
        if i == "geeks":
            yield i


# initializing string
test_string = " There are many geeks around you, \
              geeks are known for teaching other geeks"

# count numbers of geeks used in string
count = 0
print("The number of geeks in string is : ", end="")
test_string = test_string.split()

for j in print_even(test_string):
    count = count + 1

print(count)


#  -- ====== GENERATOR
generateur = (x * x for x in range(3))
for i in generateur:
    print(i)
# 0 1 4


#
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = map(lambda i: i**2, x)

while True:
    try:
        value = next(y)
        print(value)
    except StopIteration:
        print("Done !")
        break
