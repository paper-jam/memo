"""Module providingFunction printing python version."""

import os.path
import os
from glob import glob


# os.getcwd     pwd
#
# os.listdir    retuns list of dir content
# os.mkdir    difference avec os.makedirs
# os.remove
# os.rmdir
# os.removedirs
# os.rename
# os.hdir
# os.walk

variable = "Bonjour"
print(variable)

# -- os.path.splitext -> split EXTension
fichier = "C:/Python36/python.exe"
os.path.splitext(fichier)  # ('C:/Python36/python', '.exe')


# pwd
print(os.getcwd())

# change directory
os.chdir("C:\\Users\\Francis\\Google Drive\\projet\\MemoAndShortkey\\Python_Flask\\tests")

# list directory
print(os.listdir())


# make directory
if "toto" not in os.listdir():
    os.mkdir("toto")

# os.makedirs('toto4\\toto5\\toto6')

# directory must be empty for removing
os.remove("toto4\\toto5\\toto6\\test")
os.rmdir("toto4\\toto5\\toto6")
os.rmdir("toto4\\toto5")
os.rmdir("toto4")

#  dangerous
# remove all the directory of the path, they must be emty
os.removedirs("toto3\\toto4\\toto5")

# rename
os.rename(oldName="..", newName="...")
os.chdir("C:\\myfolder\\stuff\\data")
for dirpath, dirnames, filenames in os.walk("C:\\myfolder\\stuff\\data"):
    print(dirpath)  # directory path
    print(dirnames)  # list of directory
    print(filenames)  # list of files
    print("-----------")

print("==============================================")

#
for dirpath, dirnames, filenames in os.walk("C:\\Users\\francis\\toto"):
    print(dirpath)  # directory path
    print(dirnames)  # list of directory
    print(filenames)  # list of files
    print("-----------")


# os.path.join
# os.path.basename  file name file only
# os.path.dirname   dir name only of the parent file or dir
# os.path.split     dir name and file name in a tuple
# os.path.exists    return boolean
# os.path.isdir     return boolean
# os.path.isfile    return boolean
# os.path.splitext  returns tuple
# os.path.normpath  ... à étudier
# os.path.realpath  ... à etudier

# os.sep.join(liste) # defini le separateur


print(os.path.join("C:", os.environ.get("HOMEPATH"), "myfile.txt"))

# pylint : disable=line too long
pathAndNameFile = os.path.basename("C:\\Users\\Francis\\Google Drive\\projet\\MemoAndShortkey\\Python_Flask\\tests\\sample.txt")
print(pathAndNameFile)
dirName = os.path.dirname("C:\\Users\\Francis\\Google Drive\\projet\\MemoAndShortkey\\Python_Flask\\tests\\sample.txt")
print(dirName)

#  os.path.split ->  tuple (dir, filename)
dirAndFileName = os.path.split("C:\\Users\\Francis\\Google Drive\\projet\\MemoAndShortkey\\Python_Flask\\tests\\sample.txt")
("C:\\Users\\Francis\\Google Drive\\projet\\MemoAndShortkey\\Python_Flask\\tests\\", "sample.txt")


print(os.path.exists("c:\\blabla"))

# other methods :
print("isdir ->" + str(os.path.isdir("C:\\Users\\Francis\\Google Drive\\projet\\MemoAndShortkey\\Python_Flask\\tests")))

# os.path.isfile
print("isfile ->" + str(os.path.isfile("C:\\Users\\Francis\\Google Drive\\projet\\MemoAndShortkey\\Python_Flask\\sample.txt")))

# os.path.splitext
print("splitext ->" + str(os.path.splitext("C:\\Users\\Francis\\Google Drive\\projet\\MemoAndShortkey\\Python_Flask\\sample.txt")))


pathFile = "C:\\Users\\Francis\\Google Drive\\projet\\MemoAndShortkey\\Python_Flask\\sample.txt"

myfile = open(pathFile)
content = myfile.read()

myfile.seek(0)  # repert depuis le début
# content_all_line = myfile.readlines() # return a list
# # print(type(content_all_line) ) # List
# # print(content_line)
myfile.close()


pathFile = "sample.txt"

f = open(pathFile, mode="r+")
print(f.tell())
f.read()
print(f.tell())
f.write("\nXxxxx")
f.close()

#  -- with open and CLOSE the file
# -- mode = 'a' =>  open for writing, appending to the end of the file if it exists
# -- mode = 'w' =>  open for writing, no appending ! delete content if exists
# -- mode = 'r+' =>  open for reading and also writing, but writing
with open(pathFile, mode="r+") as myfile:
    myfile.write("ceci est un aussi ajout")
    myfile.read()
    myfile.read()


# ----- placer toutes les lignes d'un fichier dans une liste
names = [line.strip() for line in open("names.txt", "r")]


# ---- =========== glob library

# ---- lister les fichiers txt dans une arbo
fichiers = glob(f"{os.getcwd()}\\**\\*.txt", recursive=True)

#  --------- recherche d'un fichier dans une arborescence avec la lib glob
fichiers = glob(os.getcwd() + "\**", recursive=True)
fichiers_trouves = [f for f in fichiers if os.path.split(f)[1] == "fichier.txt"]

# ------- nombre de dossiers ds une arbo
fichiers = glob(f"{os.getcwd()}\\**", recursive=True)
print(len(fichiers))
