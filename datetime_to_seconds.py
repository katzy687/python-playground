from datetime import datetime


def get_current_ms_timestamp():
    now = datetime.utcnow()
    epoch = datetime(1970, 1, 1)
    delta = now - epoch
    s = delta.total_seconds()
    ms = int(s * 1000)
    return ms


current_ms_timestamp = get_current_ms_timestamp()
current_dt = datetime.utcfromtimestamp(current_ms_timestamp / 1000)

print current_ms_timestamp
print current_dt


