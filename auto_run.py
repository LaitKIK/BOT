import os
import subprocess
import sys
import getpass
import git

directory  =  "sites"
parent_dir =  "/home"
mode       =  "0644"
path       =  (parent_dir+"/"+directory)
def add_user():
    username  =  ("sites")
    password  =  getpass.getpass("1234")

    try:
        subprocess.run(['useradd', '-p', password, username ])
    except:
        print(f"Failed to add user")
        sys.exit(1)
add_user()

path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print("Directory '%s' created" %directory)

os.chown(path, "sites", "sites")

def git_clone():
    git.Git("/home/sites").clone("https://github.com/LaitKIK/BOT.git")
git_clone()

def run_dockerfile():
    os.system(" cd "+path+" && ",
    "docker build -t BOT .", 
    "docker run -d --name VC_BOT BOT ")
