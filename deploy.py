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
# Last Modified : Wed 22 Aug 2018 04:28:05 PM CEST
#
#####################################


import os
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
    os.chdir(home)
    sp.call(['git', 'clone', 'git://github.com/markus-goetz/gridka-2018.git'])

    with open('jupyter_modules.sh', 'w') as f:
        f.write("#!/usr/bin/env bash")
        for m in modules:
            f.write("module load " + m)
