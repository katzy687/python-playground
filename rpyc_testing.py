import rpyc
import subprocess
conn = rpyc.classic.connect("localhost")    # use default TCP port (18812)

# === p open with communicate is one approach ===
# proc = conn.modules.subprocess.Popen("ipconfig", stdout=subprocess.PIPE, stderr = -1)
# stdout, stderr = proc.communicate()
# print stdout.split()

# check_output is simpler
outp = conn.modules.subprocess.check_output("ipconfig")
print(outp)
