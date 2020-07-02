#!/usr/bin/python

import subprocess
import os
from collections import OrderedDict
from datetime import datetime

p = subprocess.Popen(["git", "log", "--pretty=format:'%at %s'"], cwd=os.getcwd(), stdout = subprocess.PIPE)

out, err = p.communicate()

if err is not None:    
    print(err)
    quit()

real_out=out.replace("'", "").split("\n")

last_date = datetime.fromtimestamp(0)
for it in real_out:
    time, message = it.split(' ', 1)

    date = datetime.fromtimestamp(float(time))
    
    if last_date.day == date.day:
        print("\t" + message)
    else:
        print(date.strftime("%d.%m.%Y:"))
        print("\t" + message)
        last_date = date
