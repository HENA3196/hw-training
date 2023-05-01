from lxml import etree

# create an element
root = etree.Element('root')

# create subelements
child1 = etree.SubElement(root, 'child1')
child2 = etree.SubElement(root, 'child2')

# set attributes
root.set('attr1', 'value1')
child1.set('attr2', 'value2')

# set text
child1.text = 'This is child1'
child2.text = 'This is child2'

# write to file
with open('example.xml', 'wb') as f:
    f.write(etree.tostring(root, pretty_print=True))
