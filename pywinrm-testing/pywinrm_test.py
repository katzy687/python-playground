import winrm  # pip install pywinrm
import time

ip = "192.168.65.32"
user = "administrator"
password = "Password1"
ps_script = "hostname"

s = winrm.Session(ip, auth=(user, password))

print("running command...")
try:
    response = s.run_ps(ps_script)
except Exception as e:
    print("Could not get response!")
    time.sleep(1)
    raise

if response.status_code == 0:
    print("hostname is: " + response.std_out)
else:
    exc_msg = "pywinrm response status errror. status code: {}. error: {}".format(response.status_code,
                                                                                  response.std_error)
    raise Exception(exc_msg)
