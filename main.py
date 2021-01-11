#!/usr/bin/python;

import ftplib
import pysftp

SFTP_HOST = 'pcr-services.net'
SFTP_PORT = 22
SFTP_USER = 'inbound_2'
SFTP_PASS = 'nsKsBELdmq'

# FTP_HOST = "pcr-services.net"
# FTP_HOST = "ftp.pcr-services.net"
FTP_HOST = "104.239.192.254"
FTP_USER = "inbound_2"
FTP_PASS = "nsKsBELdmq"

COM_FILENAME = "C:\\Users\\nagli\\Pictures\\Bikes\\F.jpg"
COM_FILEPATH = "C:\\Users\\nagli\\Pictures\\Cars"


def main():
    secure_ftp()


# SFTP Connections
def secure_ftp():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(SFTP_HOST, username=SFTP_USER, password=SFTP_PASS, cnopts=cnopts) as sftp:
        with sftp.cd():
            sftp.chdir('incoming')
            # sftp.put(COM_FILENAME, preserve_mtime=True)  # upload file to public/ on remote
            sftp.put_d(COM_FILEPATH, '', confirm=True,
                       preserve_mtime=True)  # upload files to public/ on remote
        sftp.close()


# FTP Only!
def plain_ftp():
    # connect to the FTP server
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    # force UTF-8 encoding
    ftp.encoding = "utf-8"

    # local file name you want to upload
    filename = "C:\\Users\\nagli\\Pictures\\Bikes\\F.jpg"
    with open(filename, "rb") as file:
        # use FTP's STOR command to upload the file
        ftp.storbinary(f"STOR {filename}", file)

    # list current files & directories
    ftp.dir()

    # quit and close the connection
    ftp.quit()


if __name__ == "__main__":
    main()
