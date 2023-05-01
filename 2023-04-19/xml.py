# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
import xml.etree.ElementTree as ET

xml_string = '<root><element>hello world</element></root>'

root = ET.fromstring(xml_string)
print(root)

tree = ET.parse('sample.xml')
root = tree.getroot()
print("root",root.tag) 
print("attb",root.attrib)

for child in root:
    print(child.tag, child.attrib)


#SUB ELEMENT
a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)