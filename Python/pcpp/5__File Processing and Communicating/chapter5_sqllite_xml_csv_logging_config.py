#  ====================== 5 - File Processing and Communicating with a Program's Environment =============
# pylint: skip-file


# ============================ 1 - Interacting with SQlite databases  ===============================

# DBMS : data security, transaction management, concurrent access, data exchange with other database systems.
# SQLite : C library, stored in one file, no separate process server, supports transactions, 32 or 64 bits
# python sqlite3 module : DB-API 2.0 compliant,  PEP 249, since python 2.5, SQL-92 with some exceptions
import sqlite3

conn = sqlite3.connect("C:\sqlite\hello.db")  # create file if doses not exist
conn = sqlite3.connect(":memory:")  # in-memory db




# creating table
c = conn.cursor()
c.execute("""CREATE TABLE tasks (id INTEGER PRIMARY KEY,name TEXT NOT NULL,priority INTEGER NOT NULL);""")
c.execute("INSERT INTO tasks (name, priority) VALUES (?,?)", ("My first task", 1))
conn.commit()
conn.close()


# execute many use a list of tuples
tasks = [
    ("My first task", 1),
    ("My second task", 5),
    ("My third task", 10),
]
c.executemany("INSERT INTO tasks (name, priority) VALUES (?,?)", tasks)


# reading data - method 2
c = conn.cursor()
for row in c.execute("SELECT * FROM tasks"):
    print(row)

# reading data - method 2 - fetchall
# The fetchall reads all records into the memory => memory issues if too many rows
# The fetchall returns a lit of tuples
# The fetchall method returns an empty list when no rows are available
c = conn.cursor()
c.execute("SELECT * FROM tasks")
rows = c.fetchall()
for row in rows:
    print(row)

# reading data - method 3 - fetchone
c = conn.cursor()
c.execute("SELECT * FROM tasks")
row = c.fetchone()
print(row)
row = c.fetchone()
print(row)
conn.close()
# ...

# updating data
c = conn.cursor()
c.execute("UPDATE tasks SET priority = ? WHERE id = ?", (20, 1))
c.commit()

# deleteting data
c = conn.cursor()
c.execute("DELETE FROM tasks WHERE id = ?", (1,))
c.commit()


# ============================ 2 - XML creating and processing XML files   ==========================

# library for XML parsing
# - xml.etree.ElementTree   : has a very simple API for analyzing and creating XML data.
# - xml.dom.minidom         : is the minimum implementation of the Document Object Model (DOM).
# - xml.sax                 : SAX is an acronym for “Simple API for XML”.

# an XML document is made up of :
# - prolog          the first (optional) line of the document. In the prolog, you can specify character encoding, e.g., <?xml version="1.0" encoding="ISO-8859-2"?> changes the default character encoding (UTF-8) to ISO-8859-2.
# - root element    the XML document must have one root element that contains all other elements.
# - elements        these consist of opening and closing tags.
# - attributes      <book title="Hamlet">

import xml.etree.ElementTree as ET

tree = ET.parse("books.xml")
root = tree.getroot()

# .fromstring() retunrs the root element from a string
root = ET.fromstring(your_xml_as_string)

# browsing the xml
print("The root tag is:", root.tag)
print("The root has the following children:")
for child in root:
    print(child.tag, child.attrib)

for book in root:
    print("Title: ", book.attrib["title"])
    print("Author:", book[0].text)
    print("Year: ", book[1].text, "")

# finding the first matching element
author = root.find("author")
print(author.text)

# finding element with iter methods, on all sublevel
for author in root.iter("author"):
    print(author.text)

# finding element only on first nested level
for book in root.findall("book"):
    print(book.get("title"))

# findall can also take an Xpath expression
for year in root.findall("./book/year"):
    print("Year: ", year.text)

# the find method return the first matching element
print(root.find("book").get("title"))

# we can modify or replace a tag 
    child.tag = 'movie'

# removing element
    child.remove(child.find('author'))
    child.remove(child.find('year'))

# set or add an attribute
    child.set('rate', '5')

# write to file (True is for adding the prolog)
    tree.write('movies.xml', 'UTF-8', True)

# creating a root and 2 sub element
root = ET.Element('data')
movie_1 = ET.SubElement(root, 'movie', {'title': 'The Little Prince', 'rate': '5'})
movie_2 = ET.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '5'})
ET.dump(root)


# ============================ 3 - CSV files reading and writing ====================================
# -CSV : Comma Separated Values
import csv
with open('contacts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(','.join(row))

# reading and storing in Dict
reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], ':', row['Phone'])

# file with no header  -> 
fieldnames = ['Name', 'Phone']
reader = csv.DictReader(csvfile, fieldnames=fieldnames)
#  NOTE: If you define more column names than the values in the file, the missing values will be None.


# creating a CSV file
with open('exported_contacts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    
    writer.writerow(['Name', 'Phone'])
    writer.writerow(['mother', '222-555-101'])
    writer.writerow(['father', '222-555-102'])
    writer.writerow(['wife', '222-555-103'])
    writer.writerow(['mother-in-law', '222-555-104'])


# quotechar and quoting in (QUOTE_MINIMAL, QUOTE_ALL, QUOTE_NONNUMERIC, QUOTE_NONE)
# ... can also be used in the reader function
writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# writing from a dictionnary 
fieldnames = ['Name', 'Phone']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # fieldnames is NOT optional !
writer.writeheader()
writer.writerow({'Name': 'mother', 'Phone': '222-555-101'})



# ============================ 4 - Logging : basics logging facility for Python======================
import logging

logger = logging.getLogger()                            # root logger
hello_logger = logging.getLogger('hello')               # hello is a child of root logger
hello_world_logger = logging.getLogger('hello.world')   # is a child of the hello logger
recommended_logger = logging.getLogger(__name__)        # it will use the current module name

# NOTE: Several calls to the getLogger function with the same name will always return the same object.

# --- logging levels
# CRITICAL 	50
# ERROR 	40
# WARNING 	30
# INFO 	    20  # not printed by default
# DEBUG 	10  # not printed by default
# NOTSET 	0   # not printed by default
logging.basicConfig()       # call basic configs
logger.critical('Your CRITICAL message')

# -- redefine level (by default WARNNG)
logger.setLevel(logging.DEBUG)

# -- basic configuration 
# by default : StreamHandler that displays logs in the console.
logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a') # logger is now a fileHandler

# NOTE: ThebasicConfig method changes the configuration of the root logger and its children who don't have their own handler defined.

# -- formatting wih the LogRecord object
FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'
logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a', format=FORMAT)
%(name)s        : name of the logger 
%(levelname)s   : level i.e. critical
%(asctime)s     : huma readable date/time
%(message)s     : log message

# -- one logger =  one or more handler, with e-level 
handler = logging.FileHandler('prod.log', mode='w')
handler.setLevel(logging.CRITICAL)
logger.addHandler(handler)

# -- adding a formatter to an handler
FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'
...
handler.setLevel(logging.CRITICAL)
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

# ============================ 5 - Config Parser : configuration file parser=========================
# like a windows .ini file
# NOTE: The whitespace at the beginning and end of keys and values is removed.

import configparser

config = configparser.ConfigParser()
print(config.read('config.ini'))

print('Sections:', config.sections(),'\n')
#  the DEFAULT section doesn't appear in the list of returned sections

# accessing key 'name' in the 'mariadb' sections
print('Database:', config['mariadb']['name']) # or config.get('mariadb', 'name')

# configParser and dict
config = configparser.ConfigParser()

dict = { ...
    'mariadb': {
        'name': 'hello', ...
}

config.read_dict(dict)
print('Database:', config['mariadb']['name'])

# creating or modifying a config file
config = configparser.ConfigParser()
config['DEFAULT'] = {'host': 'localhost'}
config['mariadb'] = {'name': 'hello', ...
with open('config.ini', 'w') as configfile:
    config.write(configfile)

# Interpolating values - placeholder in %()s
[DEFAULT]
host = localhost

[redis]
dsn = redis://%(host)s

#  ==================================================== FIN ===============================
