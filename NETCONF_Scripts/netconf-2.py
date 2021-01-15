from ncclient import Manager


router = {"host": "ios-xe-mgmt-latest.cisco.com:", "port": "10000",
         "username": "developer", "password": "Cisco12345"}

#print capabilites and close the session # hostkey_verify added for selfcreated certificate, production environment would need to check
with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
    m.close_session()