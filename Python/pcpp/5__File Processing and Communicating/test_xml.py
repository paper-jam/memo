''' python & xml '''
import xml.etree.ElementTree as ET
tree = ET.parse('books.xml')
root = tree.getroot() 

# root = ET.fromstring(country_data_as_string)

print('The root tag is:', root.tag)
print('The root has the following children:')
for child in root:
    print(child.tag, child.attrib)

print('---------------------') 

for book in root:
    print('Title: ', book.attrib['title'])
    print('Author:', book[0].text)
    print('Year: ', book[1].text)
    
    for price in book[2]:
        print('Prix:', price.text)

    print('---------------------') 

# finding element with iter methods on all level
for author in root.iter('author'):
    print(author.text)

print('---------------------') 
# finding element with iter methods only on first nested level
for book in root.findall('book'):
    print(book.get('title'))

print('------------ XPATH ---------') 
for year in root.findall("./book/year"):
    print('Year: ', year.text)

print('------------ FIND ---------') 
print(root.find('book').get('title'))





