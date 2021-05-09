import winrm

host_ip = "192.168.65.85"
user = "administrator"
password = "Password1"

s = winrm.Session(host_ip, auth=(user, password))

ps_script = "hostname"
response = s.run_ps(ps_script)

if response.status_code == 0:
    print(response.std_out)
else:
    print("the command returned an error")
    print(response.std_error)
pass