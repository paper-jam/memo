import xml.etree.ElementTree as ET


root = ET.Element('data')
movie_1 = ET.SubElement(root, 'movie', {'title': 'The Little Prince', 'rate': '5'})
movie_2 = ET.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '5'})
ET.dump(root)



# tree = ET.parse('.\\5__File Processing and Communicating\\books.xml')
# root = tree.getroot()

# for child in root:
#     child.tag = 'movie'
#     child.remove(child.find('author'))
#     child.remove(child.find('year'))
#     child.set('rate', '5')
#     print(child.tag, child.attrib)

#     for sub_child in child:
#         print(sub_child.tag, ':', sub_child.text)

# ET.dump(root)

# tree.write('movies.xml', 'UTF-8', True)

# xmlstr = ET.tostring(root, encoding='utf8', method='xml')
# print(xmlstr)