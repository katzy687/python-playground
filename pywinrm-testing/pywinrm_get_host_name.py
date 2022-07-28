import winrm
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("host_ip")
parser.add_argument("user")
parser.add_argument("password")
args = parser.parse_args()

host_ip = args.host_ip
user = args.user
password = args.password

# host_ip = "192.168.65.85"
# user = "administrator"
# password = "Password1"

s = winrm.Session(host_ip, auth=(user, password))

ps_script = "hostname"
response = s.run_ps(ps_script)


print("running winrm hostname check on ip {}, with credentials: {}/{}".format(host_ip, user, password))

if response.status_code == 0:
    print(response.std_out)
else:
    print("the command returned an error")
    print(response.std_error)
pass