
#recusrsive check sfv from source path and report



import os, re, sys, shutil, zlib
 
listCompleteSFV=[]
listIncompleteSFV=[]
listMissingSFV=[]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
 
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
                    return False
                c=crc(root+"/"+file)
                print(bcolors.OKGREEN+"      "+file+" "+c+bcolors.ENDC)
                if c.lower()!=list[1].lower() and c!="___":
                   match=False
        except:
            print ("What's wrong with "+root+"/"+filename+"?")
                
    return match
 
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
 
for i in albums:
    p=parse(i["root"],i["filename"],i["files"])
    try:
        if p==True:
            listCompleteSFV.append(i["root"])
        else:
            listIncompleteSFV.append(i["root"])
    except:
        pass

allLists=[{"title":"Complete", "data":listCompleteSFV, "count":len(listCompleteSFV)},
          {"title":"Incomplete", "data":listIncompleteSFV, "count":len(listIncompleteSFV)},
          {"title":"Missing SFV", "data":listMissingSFV, "count":len(listMissingSFV)}]

srt=sorted(allLists, key=lambda k: -k["count"])

print ("---------------------------------------------------------------------------------------------------------------------")
print srt[0]["title"]+" "+str(srt[0]["count"])
for i in srt[0]["data"]:
    print i
print ("---------------------------------------------------------------------------------------------------------------------")
print srt[1]["title"]+" "+str(srt[1]["count"])
for i in srt[1]["data"]:
    print i
print ("---------------------------------------------------------------------------------------------------------------------")
print srt[2]["title"]+" "+str(srt[2]["count"])
for i in srt[2]["data"]:
    print i
print ("---------------------------------------------------------------------------------------------------------------------")
