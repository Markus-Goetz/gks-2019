#!/usr/bin/env python3
#####################################
#
# Filename : deploy.py
#
# Projectname : GridKa Summerschool 2018
#
# Author : Oskar Taubert
#
# Creation Date : Wed 22 Aug 2018 04:08:18 PM CEST
#
# Last Modified : Wed 22 Aug 2018 04:52:27 PM CEST
#
#####################################


import os
# import pwd
import subprocess as sp


# users = ['padced17']
users = ["train{:03d}".format(i) for i in range(23, 53)]
# users = ["train{:03d}".format(i) for i in range(23, 24)]
modules = [
    "python/3.6.1",
    "keras/2.1.3",
    "mpi4py/3.0.0-openmpi_2.1.2",
    "matplotlib/2.1.0",
    "tensorflow/1.7.0-gcc_5.4.0-cuda_9.1.85"]
filename = '.jupyter_modules.sh'
filecontent = ""
filecontent += "#!/usr/bin/env bash\n"
for m in modules:
    filecontent += ("module load " + m + "\n")
with open(filename, 'w') as f:
    f.write(filecontent)

for user in users:
    # home = "/gpfs/homea/padcedu/" + user
    # pwnam = pwd.getpwnam(user)
    # os.chdir(pwnam.pw_dir)
    # sp.call(['git', 'clone', 'git://github.com/markus-goetz/gridka-2018.git'])
    # os.chown('gridka-2018', pwnam.pw_uid, pwnam.pw_gid)

    # get the repo
    print(user)
    host = user + "@juron.fz-juelich.de"
    # command = "git clone git://github.com/markus-goetz/gridka-2018.git"
    # sp.call(["ssh", host, command])


    # write the setup script

    # command = "echo " + filecontent + " > " + filename
    # sp.call(["ssh", host, command])
    sp.call(["scp", filename, host+':'])
    # os.chown(modulescript, pwnam.pw_uid, pwnam.pw_gid)
