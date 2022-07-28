import winrm

ip = "192.168.65.50"
user = "administrator"
password = "Password1"

remote_ip = "google.com"

s = winrm.Session(ip, auth=(user, password))

ps_script = "ping {}".format(remote_ip)
response = s.run_ps(ps_script)

if response.status_code == 0:
    print(response.std_out)
else:
    print("the command returned an error")
    print(response.std_error)
pass