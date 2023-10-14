import xml.etree.ElementTree as ET

vegan_products = []
vegan_products.append(('Good Morning Sunshine','cereals','OpenEDG Testing Service',9.90,'USD',))
vegan_products.append(('Spaghetti Veganietto','pasta','Programmers Eat Pasta',14.49,'EUR',))
vegan_products.append(('Fantastic Almond Milk','beverages','Drinks4Coders Inc.',19.75,'USD',))


root = ET.Element('shop')
category = ET.SubElement(root, 'category')
category.set('name','Vegan Products')

for item in vegan_products:
    product = ET.SubElement(category, 'product')
    product.set('name',item[0])

    elem = ET.SubElement(product, 'type')
    elem.text = item[1]
    
    elem = ET.SubElement(product, 'producer')
    elem.text = item[2]
    
    elem = ET.SubElement(product, 'price')
    elem.text = str(item[3])
    
    elem = ET.SubElement(product, 'currency')
    elem.text = item[4]

ET.dump(root)



# root.write('shop.xml', 'UTF-8', True)




