import os
import subprocess

starts = { "10": 0x5C6E, "15": 0x1235D, "16": 0xA2AB, "22": 0x1455F, "24": 0x47A6 }
ovlTable = open("uncomp/y9.bin", "rb").read()

for val in starts.keys():
    ramLoc = int.from_bytes(ovlTable[(int(val) * 16 + 4):(int(val) * 16 + 8)], "little")
    old = open("uncomp/overlay9_" + val, "rb")
    reading = old.read()
    old.close()
    new = open("output_overlay9_" + val, "wb")
    new.close()
    new = open("output_overlay9_" + val, "ab")
    
    pointers = []
    changes = [0]
    tally = 0
    for root, dirs, files in os.walk("./OVL_" + val):
        for file in files:
            pointers.append(int(file.split("_")[0]))
            tally = tally + (os.stat(os.path.join(root, file)).st_size - int(file.split("_")[1].split(".")[0]))
            changes.append(tally)
    
    count = 0
    while count < starts[val]:
        current = int.from_bytes(reading[count:(count + 4)], "little")
        if ((current - ramLoc) in pointers):
            new.write((current + changes[pointers.index(current - ramLoc)]).to_bytes(4, "little"))
            count = count + 4
        else:
            new.write(reading[count].to_bytes(1, "little"))
            count = count + 1
    for root, dirs, files in os.walk("./OVL_" + val):
        for file in files:
            final = open(os.path.join(root, file), "rb")
            finalRead = final.read()
            final.close()
            new.write(finalRead)
            if (files.index(file) != (len(files) - 1)):
                new.write(bytes(1))
    new.close()
    subprocess.run(["blz.exe", "-en", "output_overlay9_" + val])
        