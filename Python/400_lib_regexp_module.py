# pylint: disable=invalid-name
# pylint: disable=line-too-long
"""13_regexp.py"""

import re

# == search a sub string
txt = "The rain in spain"
x = re.findall("ai", txt)
print(x)


# == search position of a sub string 
txt = "The rain in spain"
x = txt.find("ai")
print(x)
#  ==> 5

# -- =====  check email
import re
email = 'toto@free.fr'
regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
re.search(regex, email)  # true or false







