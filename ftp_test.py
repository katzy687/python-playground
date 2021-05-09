from ftplib import FTP

FTP_SERVER_IP = "localhost"
FTP_USER_NAME = "natti"
FTP_PASSWORD = "test"
FTP_CONFIGS_DIR = "cloudshell-physical-configs"

# get ftp session
ftp = FTP(FTP_SERVER_IP, FTP_USER_NAME, FTP_PASSWORD)
ftp.cwd(FTP_CONFIGS_DIR)

if "asdf" not in ftp.nlst():
    ftp.mkd("asdf")
else:
    print("dir exists")