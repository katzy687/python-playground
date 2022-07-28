from xml.etree import ElementTree

root = ElementTree.parse("testconfig.xml").getroot()
test_model = root.find('network')
network_name = test_model.get('name')
print(network_name)