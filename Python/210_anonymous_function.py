# -- =================== fonctions anonymes
# can have any number of arguments but only one expression


cube = lambda x: x * x * x
cube(7)  # 343

multiplication = lambda x, y: x * y
multiplication(10, 5)  # 50

# -- ===== lambda
print((lambda x: x**2)(5))  # -> 25 / direct use

# -- ======= depuis la version 3
print_bonjour = lambda: print("bonjour")
print_bonjour()

print_mot = lambda mot: print(mot)
print_mot("Francis")


# ---- others examples
# Example list
my_list = [1, 2, 3, 4, 5]

# Use lambda to filter out even numbers from the list
list(filter(lambda x: x % 2 != 0, my_list))  # [1, 3, 5]
