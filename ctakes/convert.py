# import xml.etree.ElementTree as ET

# # Read the text file
# with open('./casestudy2/ir.txt', 'r') as file:
#     lines = file.readlines()

# # Create the root element
# root = ET.Element('root')

# # Add each line from the text file as a child element of the root
# for line in lines:
#     element = ET.SubElement(root, 'element')
#     element.text = line.strip()

# # Create the XML tree and write it to a file
# tree = ET.ElementTree(root)
# tree.write('./casestudy2/output.xml')

import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('./casestudy2/out/output.xml')
root = tree.getroot()

# Add the 'pos_start' attribute to each 'element' tag
for element in root.iter('element'):
    element.set('pos_start', 'your_value')

# Write the modified XML back to the file
tree.write('./casestudy2/out/ele.xml')
