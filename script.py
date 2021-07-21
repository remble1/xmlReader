import xml.etree.ElementTree as ET

xmlfile = 'Cars0.xml'

tree = ET.parse(xmlfile)
root = tree.getroot()

#ET.dump(tree)

for elm in root.iter("bndbox"):
    xmin = elm.find('xmin').text
    xmax = elm.find('xmax').text
    ymin = elm.find('ymin').text
    ymax = elm.find('ymax').text
    #xmax = elm.find()
    print(xmin, xmax, ymin, ymax)


