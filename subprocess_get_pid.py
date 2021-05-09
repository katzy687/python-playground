import subprocess
import time
import psutil
import os


def start_process():
    """
    Starts a process in the background and return pid
    returns integer: pid
    """
    # Start process
    process = subprocess.Popen('notepad.exe')
    return process.pid


def kill_process(pid):
    """ No external libraries needed for this one"""
    import os
    import signal

    os.kill(pid, signal.SIGTERM)


def psutil_kill(pid):
    p = psutil.Process(pid)
    p.terminate()


def _kill_my_clt(pid):
    name = "notepad"
    processes = []
    for process in psutil.process_iter():
        name_, exe, cmdline = "", "", []
        try:
            name_ = process.name()
            cmdline = process.cmdline()
            exe = process.exe()
        except (psutil.AccessDenied, psutil.ZombieProcess, OSError, SystemError):
            pass
        except psutil.NoSuchProcess:
            continue
        if name in name_ and process.pid == pid:
            processes.append(process)
    if processes:
        processes[0].kill()


pid = start_process()
time.sleep(3)

# kill_process(pid)
# psutil_kill(pid)
_kill_my_clt(pid)