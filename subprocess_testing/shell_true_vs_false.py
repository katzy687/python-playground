from subprocess import PIPE, Popen

process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
