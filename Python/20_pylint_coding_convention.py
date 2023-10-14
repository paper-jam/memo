# --------- coding convention
# pylint: disable=invalid-name

# indentation with 4 spaces (not tabs), encoding UTF8, max line lenght 79
# with open('/path/to/some/file/you/want/to/read') as file_1, \
#      open('/path/to/some/file/being/written', 'w') as file_2:
#     file_2.write(file_1.read())
# import on different lines, order is :
#   1 - Standard library imports.
#   2 - Related third party imports.
#   3-  Local application/library specific imports.

# # line break before operators
# income = (gross_wages
#           + taxable_interest
#           + (dividends - qualified_dividends)
#           - ira_deduction
#           - student_loan_interest)
# More info here: https://realpython.com/python-pep8/




# -------- pylint ----------------
# messages type
    # C convention related checks
    # R refactoring related checks
    # W various warnings
    # E errors, for probable bugs in the code
    # F fatal, if an error occurred which prevented pylint from doing further processing.

# 0 - at the root block first level of a file 

# 1 - in file pylintrc
# in line method
var1 = "bonjour"  #### # p y l int: disable=C0103

# on the next line
# pylint: disable-next=line-too-long
var2 : str = "bonjour " + "bonjour " + "bonjour " + "bonjour " + "bonjour " + "bonjour " + "bonjour " + "bonjour "

# in a block scope
def test():
    ''' docstring '''
    # Disable all the no-member violations in this function
    # pylint: disable=no-member
