import json
from collections import OrderedDict

my_dict = {
    "service_alias": "Interface Config",
    "vlan_id": "5",
    "switchport_mode": "access",
    "interfaces": [
        {
            "root_switch": "quali_virtual_nxos_switch",
            "interface": "Eth2/1",
            "connected_to": "mock_6/Port 3"
        }
    ],
}

order_of_keys = ["service_alias", "vlan_id", "switchport_mode", "interfaces"]
list_of_tuples = [(key, my_dict[key]) for key in order_of_keys]
your_dict = OrderedDict(list_of_tuples)

json_str = json.dumps(your_dict, indent=4, sort_keys=False)
print(json_str)
