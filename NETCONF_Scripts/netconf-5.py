from ncclient import Manager
from pprint import pprint
import xmltodict
import xml .dom.minidom
from router_info import router
#import logging
#logging.basicConfig(level=logging.DEBUG)

netconf_filter = open(
    "C:\Users\Georj\OneDrive\Documents\GitHub\PythonScripts\PythonScripts\NETCONF_Scripts\netconf-filter.xml").read()

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
    #get the running config on the filtered out interface
    print('Connected')
    interface_netconf = m.get(netconf_filter)
    print('getting running config')
# below, xml is a property of interface_conf

# XMLDOM for formatting output to xml
XMLDOM = xml.dom.minidom.parseString(str(interface_netconf))
print(xmlDom.toprettyxml(indent="  "))
print('*' * 25 + 'Break' + '*' * 50)
# XMLTODICT for converting xml output to a python dictionary
interface_python = xmltodict.parse(interface_netconf.xml)[
    "rpc-reply"]["data"]
pprint(interface_python)
name = interface_python['interfaces']['interface']['name']['#text']
print(name)

config = interface_python['interfaces']['interface']
op_state = interface_python['interfaces-state']['interface']

print("Start")
print(f"name: {config['name']['#text']}")
print(f"description: {config['description']}")
print(f"Packets In {op_state['statistics']['in-unicast-pkts']}")