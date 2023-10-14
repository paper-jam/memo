#  ---- ======================  les tuples

# Tuple is a collection which is ordered and immutable. Allows duplicate members.

# ---- declare
t1 = ()
t1 = tuple()
t1 = ("apple",)  # tuple avec un seul élément : ne pas oublier la virgule !!
t1 = "chat", "chien", "raton", [1, 2, 3, 4]  # parentheses facultatives !
t1 = (1,)  # 1 seul élémen et pas de parenthèse
t1 = ("chat",)  # ne pas oublier la virgule
t2 = ("apple", "banana")

t1 = (1, 2, 3, "francis", "francis", [1, 2, 3])  # heterogeneous, duplicate items


# ---- access
t1[2]  # -> 3 -  !! IndexError: tuple index out of range
t1.index("francis")  # index(str, start, end)

t2 = t1[:3]  #  tuple -> (1, 2, 3), so  slicing is OK !
# ----  unchangeable : => no removing, no add, no modify

# ---- other methods
t1.count("francis")  # 2
len(t1)  # 6

# -- sorting  a tuple
tuple(sorted(t1))

# ----- concatening tuples
t2 = (1, 2, 3) + (3, 4, 5)
t3 = t2 * 2  # (1, 2, 3, 3, 4, 5, 1, 2, 3, 3, 4, 5)

# -----  tuples comparison
x = ("1", "2")
y = ("1", "3")
x == y  # True
y > x  # True

x = ("1", "2")
y = ("1", "2")


# -----  comparing
data1 = "a", "b"
data2 = ("a", "b")
print(data1 == data2)


# -- ===== iterating on a list of tuple
users = [("bob", 12, 1), ("carine", 50, 2), ("francis", 100, 3)]

for name, salary, nb_cars in users:
    print(name + "--->" + str(salary) + "/" + str(nb_cars))

# fin
