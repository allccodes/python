
#!/usr/bin/env python3
# Copyright 2018 Bastard Operator
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This script will get a specific URL and either return basic information
# about the site or will throw out an error that URL does not exist.
# Seems to work even when using a proxy server, but it times out on some
# sites, not sure why.


import argparse
import subprocess
import paramiko
import os
import logging


parser = argparse.ArgumentParser(description="Upload or Download files to SFTP Server")
parser.add_argument("args", help="Argument to be passed to the script")
args = parser.parse_args()
 

host="hostname"
username="username"
password="password"



def download():

    local_path = r'C:\Users\Desktop\Ftps'
    log_path = r'C:\Users\Desktop\ftp_download.log'


    logging.basicConfig(filename=log_path, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')


    with paramiko.SSHClient() as ssh:
        ssh.load_system_host_keys()
        ssh.connect(host, username=username, password=password)
    
        sftp = ssh.open_sftp()
        sftp.chdir('downloads')
        list_files=sftp.listdir()

        total = 0
        for file in list_files:
            local_file_path = os.path.join(local_path, file)
            try:
                sftp.get(file, local_file_path)
                total +=1
            except Exception as e:
                logging.error(f"Failed to download {file} to {local_file_path}: {e}")
       

    print(f"Number of files transferred: {total}")



def upload():

    local_path = r'C:\Users\Desktop\Ftps'
    log_path = r'C:\Users\Desktop\Ftps\ftp_upload.log'

    logging.basicConfig(filename=log_path, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')



    with paramiko.SSHClient() as ssh:
        ssh.load_system_host_keys()
        ssh.connect(host, username=username, password=password)
    
        sftp = ssh.open_sftp()
        sftp.chdir('uploads')

        total = 0
        for file in os.listdir(local_path):
            local_file_path = os.path.join(local_path, file)
            if os.path.isfile(local_file_path):  
                try:
                    sftp.put(local_file_path, file)
                    logging.info(f'Successfully uploaded {local_file_path} to {file}')
                    total += 1
                except Exception as e:
                    print(f"Failed to upload {local_file_path}: {e}")
            else:
                logging.warning(f'Skipping {file}: not a file')


    print(f"Number of files transferred: {total}")



# START HERE

match args.args:
    case "download" | "Download":
        print("Downloading files...")
        download()
    case "upload" | "Upload":
        print("Uploading files...")
        upload()
    case _:
        print("Invalid Option! Example: ./ftp.py [download][upload]")

 
