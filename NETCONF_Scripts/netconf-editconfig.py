from ncclient import Manager
from router_info import router

config_template = open(
    'C:\Users\Georj\OneDrive\Documents\GitHub\PythonScripts\PythonScripts\NETCONF_Scripts\iosconfig.xml').read()

netconf_config = config_template.format(
    interface_name="GigabitEthernet2", interface_desc="Knox wuz here")

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    device_reply = m.edit_config(netconf_config, target="running")
    print(device_reply)