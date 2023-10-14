#  ============================= 2 Best_Practises_and_Standardization =============================
# pylint: skip-file

# PEP stands for Python Enhancement Proposals

#  Pep was a nickname of a famous football manager Josep Guardiola,

# PEP 1 – PEP Purpose and Guidelines
#       information about the purpose of PEPs, their types, and introduces general guidelines

# PEP 8 – Style Guide for Python Code
#         conventions and presents best practices for Python coding;
# PEP 20 – The Zen of Python
#          list of principles for Python’s design
# PEP 257 – Docstring Conventions,
#           guidelines for conventions and semantics associated with Python docstrings.

# ----------PEP 1 - PEP Purpose and Guidelines

# Standards Track PEPs  : new language features and implementations;
# Informational PEPs    : Python design issues, as well as provide guidelines and information to the Python community;
# Process PEPs          : which describe various processes that revolve around Python (e.g., propose changes, provide recommendations, specify certain procedures

# the members
# - Python’s Steering Council, i.e., a five-person
# - Python’s Core Developers, i.e., the group of volunteers who manage Python, and;
# - Guido van Rossum, Benevolent Dictator For Life,  until 2018

# PEP champion – someone who writes a PEP proposal, and attempts to build community consensus

# ---------- PEP 20 - the zen of Python
# 19 lines poems from Tim Peters
import this

# Beautiful is better than ugly
# Simple is better than complex
# Complex is better than complicated
# Explicit is better than implicit =>   apples(2, 3.45) => apples(quantity=2, price=3.45)
# Flat is better than nested ==> avoid many level of imbrication if.. if... loop..
# Sparse is better than dense : don't write lines too long
# Readability counts
# Special cases aren't special enough to break the rules => Discipline, consistency, and compliance with standards and convention
# Although, practicality beats purity : rules can be broken for good reasons
# Errors should never pass silently : use exceptions
# In the face of ambiguity, refuse the temptation to guess :  avoid writing ambiguous code, test code, limited trust in the code you’re reading
# There should be one – and preferably only one – obvious way to do it
# Now is better than never
# If the implementation is hard to explain, it's a bad idea
# Namespaces are one honking great idea – let's do more of those!


# ---------- PEP 8 – Coding conventions

# our code will be read much more often than it will be written.
# PEP 8 compliant checkers : pycodestyle / autopep8 (requires pycodestyle) / PEP 8 online


# -- indentaion
# 4 spaces per indentation level (no tabs -> tabErrorException)
# 79 caracteres per line
# break before binary operators
total_fruits = (apples
                + pears
                + grapes
                - (black currants - red currants)
                - bananas
                + oranges)

# -- blank lines
# two blank lines to surround top-level function and class definitions
# a single blank line to surround method definitions inside a class
# blank lines in functions in order to indicate logical sections

# -- encoding
# Python’s default encodings (Python 3 -- UTF-8, Python 2 -- ASCII

# -- import
# imports at the beginning of your script
# imports be on separate lines
# absolute imports is OK (import animals.mammals.dogs.puppies), avoid wildcards: from module import *
# order : 1-Standard library 2-Related third-party imports 3- Local application/library specific.
# explicit is better than implicit
from fruit import apples, bananas

apples(quantity=2, price=3.45)

# String : avoid using backslashes as possible
# -- spaces
# writing code : space after comma/semicolon/colon only
# not use excessive whitespace
# Don’t surround the = operator with spaces if it’s used to indicate a keyword argument
my_tuple = (0, 1, 2,)
def my_function(x, y=2):
    x = (x-1) * (x+2)


# -- naming conventions
MY_SAMPLE_CONSTANT = 5.96
my_variable = 1
def my_function():
    pass
class MySampleClass:
    PI = 3.14
    def my_class_method():
        pass
# module -> lower case with underscore : my_module.py
# module -> lower case with NO underscore : package
# Exception -> camelCase

# -- naming convntions for class name
# - Class names should normally use the CapWords convention.
# - The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.
# - Note that there is a separate convention for builtin names: most builtin names are single words (or two words run together), with the CapWords convention used only for exception names and builtin constants.




# ----- comments :
# complete sentences, capitalize the first word, end with dot > "Program that calculates body mass index (BMI)."
# comments should be 72 characters per line
# Block comments : refer to the code that follows them, with same indentation level
# inline comments : separated with 2 spaces, use them sparingly
# docstrings """ """ pep 257 for all public modules, files, functions, classes, and methods

# naming convention
#   my_sample_name_  to avoid any conflicts with Python keywords, e.g., class_
#   _my_sample_name  weak "internal use",  import * do not import objects starting with an underscore.

# PEP8 conventions => ma_variable, MySampleClass, my_class_method, MY_CONSTANT, self and cls for parameters
# PEP8 conventions => module.py my_module (shortname), package, mypackage (shortname), TankException

# Other recommandations :
if var_boolean:  # instead of : if var_boolean == True
if x is not None: # instead of : if not x is None:
except ZeroDivisionError # instead of :  except Exception: (use specific exception, when possible)
if name.startswith('Adam'):# instead of : if name[:4] == 'Adam':


# ---------- PEP 257 – Docstrings conventions
# https://peps.python.org/pep-0257/



# ------------- just  a focus on type hinting - PEP 484
def hello(name: str) -> str:
# - is not used at runtime, no impact on performance
# - participate to documentation and code cleaner
# - allows helping features in editor or IDE, like auto-completion


# for module, function, class, or method definition
# docstring becomes the __doc__ attribute, can be reach also with the help() function


# comments are used for commenting your code,
# docstrings are used for documenting your code

# docstring limited at 72 characters

# Why use comments :
# - for TODO
# - for commenting code
# - for planning code to write


# 2 kinks of 'extra' docstrings :
# - attribute docstrings : top level of module,class, or __init__
# - additional dosctrings, located immediately after another docstring

# dealing with special character
# - r"""raw triple double quotes"""  # if presence of backslashes in the docstring
# - u"""Unicode triple-quote strings""" # if presence of unicode in the docstring

# it starts with a Uppercase and and with a period. It takes the form of an imperative.
# docstring should be indented to the same level as the open quotes and code following
def greeting(name):
    """Take a name and return its replicated form."""
    return name * 2


# two different docstring formats for documenting
# - reStructuredText, and it's the official Python documentation standard
# - NumPy/SciPy format
# both are compatible with the Sphinx tools, for creating documenation


# Generally, a project should contain the following documentation elements:
# - a readme
# - an examples.py a few examples of how to utilize the project;
# - a license for Open Source sharing
# - a how to contribute file

# a linter
# -  stylistic anomalies and programming errors against a set of pre-defined rules
# -  Flake8, Pylint, Pyflakes, Pychecker, Mypy, and Pycodestyle


# a fixer
# - fix these issues and format your code to be consistent with the adopted standards.
# - Black, YAPF, and autopep8.


#  --------------------------- FIN --------------------------------
