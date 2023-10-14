import xml.etree.ElementTree as ET


tree = ET.parse('.\\5__File Processing and Communicating\asa.xml')
root = tree.getroot()


for dataset in root :
    print(dataset[0].text)
    