import os
import shutil
import subprocess

starts = { "10": 0x5C6E, "15": 0x1235D, "16": 0xA2AB, "22": 0x1455F, "24": 0x47A6 }
try:
    shutil.copytree("./root/ftc", "./uncomp")
    for i in range(30):
        subprocess.run(["blz.exe", "-d", "uncomp/overlay9_" + str(i) ])
    os.remove("uncomp/rom.nds")
except:
    pass
    
for val in starts.keys():
    try:
        os.mkdir("OVL_" + val)
    except:
        pass
    file = open("uncomp/overlay9_" + val, "rb")
    reading = file.read()
    file.close()
    data = list(reading[starts[val]:].split(bytes(1)))
    loc = starts[val]
    for string in data:
        new = open("OVL_" + val + "/" + str(loc).zfill(6) + "_" + str(len(string)) + ".txt", "wb")
        new.write(string)
        new.close()
        loc = loc + len(string) + 1