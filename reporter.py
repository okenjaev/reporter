#!/usr/bin/python

import subprocess
import os
from datetime import datetime

def systemCall(args):
    p = subprocess.Popen(args, cwd = os.getcwd(), stdout = subprocess.PIPE, universal_newlines=True)
    out, err = p.communicate()
    if err is not None:
        print(err)
        quit()
    else:
        return out

author = systemCall(["git", "config", "user.name"]).replace('\n', '').replace('\'', '')
print("Generating report for user " + author)

today = datetime.today()

args = ["git",
        "--no-pager",
        "log",
        "--since=\"{0}-{1}-01\"".format(today.year, today.month),
        "--no-merges",
        "--pretty=format:%an, %at, %s"]

real_out = systemCall(args).split('\n')
last_date = datetime.fromtimestamp(0)

for it in real_out:
    committer, time, message = it.split(', ',2)
    if committer != author:
        continue
    
    date = datetime.fromtimestamp(float(time))
    
    if last_date.date() == date.date():
        print("\t " + message)
    else:
        print(date.strftime("%d.%m.%Y:"))
        print("\t " + message)
        last_date = date
