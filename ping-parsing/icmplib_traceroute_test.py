import json

from icmplib import ping, multiping, traceroute, resolve, Hop

TARGET_IP = "google.com"

tr_hops = traceroute(address=TARGET_IP)
full_output = "\n".join([str(hop) for hop in tr_hops])
print(full_output)