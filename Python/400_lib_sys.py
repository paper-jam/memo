import sys
import functools

sys.float_info  # sys.float_info(max=1.7976931348623157e+308, ...
sys.int_info  # sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300

sys.maxsize  # 9223372036854775807 # In Python 3, the int type has no max limit.

# ----- récupération d'arguments PEP
# avec  python application.py test1 test2
sys.argv  # ['application.py', 'test1', 'test2']
len(sys.argv)  # 3 - nombre d'arguments
sys.argv[0]  # premier   argument = nom du programme
sys.argv[1]  # test1
sys.argv[2]  # test2


sys.version  # 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)]'
sys.path  # a built-in variable within the sys module that returns the list of directories that the interpreter will search for the required module.
sys.executable  # 'C:\\appli\\python\\python310\\python.exe'
sys.modules  # tous les modules importés
sys.platform  # 'win32', 'linux'
sys.exit("Age less than 18")  # exit the program


sys.stdout  # is associted with screen, by default

# get memory size
var = range(100)
sys.getsizeof(var)


# -- ======= path for library search
print(sys.path)
print(sys.executable)
