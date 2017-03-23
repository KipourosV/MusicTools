
#recusrsive duplicates search

import os, re, sys, shutil, subprocess
from fuzzywuzzy import fuzz, process
from pprint import pprint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
 

albums=[]
for root, dirs, files in os.walk(sys.argv[1]):
    albums.append({ "last": root.split("/")[-1], "full":root})

dupes={}
checked={}

for i in albums:
    temp=[]
    for j in albums:
        if i["full"]==j["full"]: continue
        ratio=fuzz.ratio(i["last"],j["last"])
        if ratio > 85:
            temp.append({"root": j["full"], "ratio": ratio})
            checked[j["full"]] = True
    if len(temp)>0 and not i["full"] in checked:
        temp.append({"root": i["full"], "ratio": 0})
        dupes[i["last"]]=temp

print len(dupes.keys())
for k in dupes:
    for i in dupes[k]:
        subprocess.Popen(["xdg-open", i["root"]])
    print("\n\nPress any key for next batch...")
    raw_input()

