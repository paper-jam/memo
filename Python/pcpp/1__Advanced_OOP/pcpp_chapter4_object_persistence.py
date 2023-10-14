# ================================= Object persistence ==================
# pylint: skip-file

# ------------------------------------ id shallow and deep copy -----
# id() is is the address of the object in the memory
# avoid naming a variable as id
# a shallow copy is only one level deep
# deep copy might cause problems when there are cyclic references in the structure to be copied
# a deep copy operation takes significantly more time than any shallow copy operation;
import copy

l1 = ["a", [1, 2, 3]]
shallow_copy_list = copy.copy(l1)
deep_copy_list = copy.deepcopy(l1)

# a deep copy is really deep
l1 = [1, 2, ["Arthur", "Bob", {"pays": ["France", "Italie"]}]]
l2 = copy.deepcopy(l1)
l2[2][2]["pays"][1] = "Belgique"
# l1 ==> [1, 2, ['Arthur', 'Bob', {'pays': ['France', 'Italie']}]]
# l2 ==> [1, 2, ['Arthur', 'Bob', {'pays': ['France', 'Belgique']}]]

# ------------------------------------ Serialization with pickle ----------------
# types that can be pickled
# None, booleans, integers, floating-point numbers, complex numbers, strings, bytes, bytearrays;
# tuples, lists, sets, and dictionaries containing pickleable objects;
# objects, including objects with references to other objects (remember to avoid cycles!)
# references to functions and classes, but not their definitions.

# main method are : import pickle, pickle.dump(), pickle.load()
# for serialized object : pickle.dumps() and pickle.loads()
# the order in which the objects were persisted (dump)
# and the deserialization (.load) code should follow the same order.

# non-pickleable objects will raise the PicklingError exception
# pickling a function or class, pickles only the name, not the code
# avoid pickling highly recursive data structure -> 'RecursionError'
# 'AttributeError' if function/class code in missing when reading the pickle file

# picke module is a Python implementation, not compatible with Java/C++ .. => use JSON or XML
# use the same version of pickel for serializing and deserializing !

import pickle

a_list = ["a", 123, [10, 100, 1000]]
bytes = pickle.dumps(a_list)
print("Intermediate object type, used to preserve data:", type(bytes))

# now pass 'bytes' to appropriate driver

# therefore when you receive a bytes object from an appropriate driver you can deserialize it
b_list = pickle.loads(bytes)
print("A type of deserialized object:", type(b_list))
print("Contents:", b_list)


# ------------------------------------ Serialization with shelve-----
# objects are pickled and associated with a key. The keys must be ordinary strings.
# then the order in which objects are serialized no more matters

# 'r'   Open existing database for reading only
# 'w'   Open existing database for reading and writing
# 'c'   Open database for reading and writing, creating it if it doesn’t exist (this is a default value)
# 'n'   Always create a new, empty database, open for reading and writing

# sync() or close() flush the buffers
# shelve is a dict, so we can use : len(), in, keys(), items(), update(), del()

import shelve

shelve_name = "first_shelve.shlv"

my_shelve = shelve.open(shelve_name, flag="c")
my_shelve["EUR"] = {"code": "Euro", "symbol": "€"}
my_shelve["GBP"] = {"code": "Pounds sterling", "symbol": "£"}
my_shelve["USD"] = {"code": "US dollar", "symbol": "$"}
my_shelve["JPY"] = {"code": "Japanese yen", "symbol": "¥"}
my_shelve.close()

new_shelve = shelve.open(shelve_name)
print(new_shelve["USD"])
new_shelve.close()

# ------------------------------------  fin  -----------------------------
