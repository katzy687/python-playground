import subprocess
from subprocess import Popen, PIPE

# s = subprocess.check_output(["cmdkey /generic:'1.1.1.1' /user:'user_test' /pass:'super_secret'"])

# process = Popen(['cmdkey', '/generic:1.1.1.1', '/user:user_test', '/pass:super_secret'], stdout=PIPE, stderr=PIPE)
# stdout, stderr = process.communicate()
# print stdout

# s = subprocess.check_output(['cmdkey', '/generic:1.1.1.1', '/user:user_test', '/pass:super_secret'])
# print s

x = subprocess.check_output(['mstsc', '/v:1.1.1.1'])
print x