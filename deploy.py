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
import pwd
import subprocess as sp


users = ['padced17']
modules = [
    "python/3.6.1",
    "keras/2.1.3",
    "mpi4py/3.0.0-openmpi_2.1.2",
    "matplotlib/2.1.0",
    "tensorflow/1.7.0-gcc_5.4.0-cude_9.1.85"]

for user in users:
    home = "/gpfs/homea/padcedu/" + user
    pwnam = pwd.getpwnam(user)
    os.chdir(pwnam.pw_dir)
    sp.call(['git', 'clone', 'git://github.com/markus-goetz/gridka-2018.git'])
    os.chown('gridka-2018', pwnam.pw_uid, pwnam.pw_gid)

    modulescript = '.jupyter_modules.sh'
    with open(modulescript, 'w') as f:
        f.write("#!/usr/bin/env bash")
        for m in modules:
            f.write("module load " + m)
    os.chown(modulescript, pwnam.pw_uid, pwnam.pw_gid)
