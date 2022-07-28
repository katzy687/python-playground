import xml.etree.ElementTree as etree
from xml.etree.ElementTree import Element

# XML_PATH = "testshell edit app.xml"
XML_PATH = "empty_blueprint.xml"
XML_PATH = "branch_service.xml"


PARENT_BLUEPRINT_ID_ATTR_NAME = "Branch Service.Parent Blueprint ID"
GIT_BRANCH_ATTR_NAME = "Branch Service.Git Branch Name"


# create element tree object
tree = etree.parse(XML_PATH)

# get root element
root = tree.getroot()
services_node_search = root.findall("Services")

if not services_node_search:
    etree.SubElement(root, "Services")

services_node = services_node_search[0]


def add_branch_service(parent_blueprint_id, git_branch_name):
    # add service node
    service_node_attrs = {"PositionX": "100", "PositionY": "259", "Alias": "Branch Service", "ServiceName": "Branch Service"}
    service_node = etree.SubElement(services_node, "Service", service_node_attrs)

    # add attributes
    etree.SubElement(service_node, "Attribute", {"Name": PARENT_BLUEPRINT_ID_ATTR_NAME, "Value": parent_blueprint_id})
    etree.SubElement(service_node, "Attribute", {"Name": GIT_BRANCH_ATTR_NAME, "Value": git_branch_name})


def update_branch_service(service_elm: Element , parent_blueprint_id: str, git_branch_name: str):
    attrs_container = service_elm.findall("Attributes")[0]
    attrs = attrs_container.findall("Attribute")
    for attr in attrs:
        if attr.attrib["Name"] == PARENT_BLUEPRINT_ID_ATTR_NAME:
            attr.attrib["Value"] = parent_blueprint_id
        elif attr.attrib["Name"] == GIT_BRANCH_ATTR_NAME:
            attr.attrib["Value"] = git_branch_name



branch_service_search = [x for x in services_node.findall("Service") if x.attrib["ServiceName"] == "Branch Service"]
if not branch_service_search:
    add_branch_service("asdf", "feature1")
else:
    update_branch_service(branch_service_search[0], "qwer", "feature2")
etree.dump(root)
pass