
#recusrsive check sfv from source path and report



import os, re, sys, shutil, zlib
 
listCompleteSFV=[]
listIncompleteSFV=[]
listMissingSFV=[]
listNew=[]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getState(files):
    for f in files:
        if f == ".sfvcomplete": return "complete"
        if f == ".sfvincomplete": return "incomplete"
        if f == ".sfvmissing": return "missing"
    return "new"

def setState(root,state):
    if state=="new": return
    try:
        os.remove(root+"/.sfvcomplete")
        os.remove(root+"/.sfvincomplete")
        os.remove(root+"/.sfvmissing")
    except:
        pass
    f=open(root+"/.sfv"+state,"w")
    f.close()

def crc(fileName):
    prev=0
    try:
        store=open(fileName, "rb")
    except:
        return "___"
    for eachLine in store:
        prev = zlib.crc32(eachLine, prev)
    store.close()
    s = "%08X"%(prev & 0xFFFFFFFF)
    return s

def parse(root,filename,files):
    print("\n "+root)
    try:
        store=open(root+"/"+filename, "r")
    except:
        print (bcolors.FAIL+"Failed to open source SFV file "+root+"/"+filename+bcolors.ENDC)
        return False
    match=True

    for line in store:
        list=line.split(" ")
        if len(list) != 2: continue
        list[1]=list[1].rstrip('\r\n');
        try:
            if len(list)==2 and list[0][0]!=";":
                file=False
                for f in files:
                    if list[0].lower()== f.lower():
                        file=f
                        break
                if file==False:
                    print (bcolors.FAIL+"File missing"+bcolors.ENDC)
                    return False
                c=crc(root+"/"+file)
                print(bcolors.OKGREEN+"      "+file+" "+c+bcolors.ENDC)
                if c.lower()!=list[1].lower() and c!="___":
                   match=False
                   print (bcolors.FAIL+"CRC failed"+bcolors.ENDC)
        except:
            print ("What's wrong with "+root+"/"+filename+"?")

    return match

if len(sys.argv)>2:
    filter=sys.argv[2]
else:
    filter=False


albums=[]
for root, dirs, files in os.walk(sys.argv[1]):
    lst2=root.split("/")
    l=len(lst2)
    foundsfv=False
    for f in files:
        list=f.split(".")
        if len(list)>0 and list[-1]=="sfv":
            foundsfv=True
            albums.append({
                "root":root,
                "filename":f,
                "count":l,
                "target":lst2[-1],
                "files":[x for x in files],
                "dircount":len(dirs)
            })
    if not foundsfv:
        listMissingSFV.append(root)
        setState(root,"missing")

for i in albums:
    state=getState(i["files"])
    if state=="new":
        listNew.append(i["root"])

    if filter == False or filter != state: 
        if state=="complete":
            listCompleteSFV.append(i["root"])
        elif state=="incomplete":
            listIncompleteSFV.append(i["root"])
        continue

    p=parse(i["root"],i["filename"],i["files"])
    try:
        if p==True:
            listCompleteSFV.append(i["root"])
            setState(i["root"],"complete")
        else:
            listIncompleteSFV.append(i["root"])
            setState(i["root"],"incomplete")
    except:
        pass

allLists=[{"title":"Complete", "data":listCompleteSFV, "count":len(listCompleteSFV), "state":"complete"},
          {"title":"Incomplete", "data":listIncompleteSFV, "count":len(listIncompleteSFV), "state":"incomplete"},
          {"title":"Missing SFV", "data":listMissingSFV, "count":len(listMissingSFV), "state":"missing"},
          {"title":"New", "data":listNew, "count":len(listNew), "state":"new"}]

srt=sorted(allLists, key=lambda k: -k["count"])

for j in range(0,len(srt)):
    print ("---------------------------------------------------------------------------------------------------------------------")
    print srt[j]["title"]+" "+str(srt[j]["count"])
    for i in srt[j]["data"]:
        print i

for j in range(0,len(srt)):
    print ("---------------------------------------------------------------------------------------------------------------------")
    print srt[j]["title"]+" "+str(srt[j]["count"])

