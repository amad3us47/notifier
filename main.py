import os
import time
import requests
import filecmp
import shutil
import difflib
from datetime import datetime
file1="C:\\Users\\chotu\\Desktop\\stocks\\o.txt"
file2="C:\\Users\\chotu\\Desktop\\stocks\\new.txt"
header = {
    'authorization': 'MTE3NzI2NjM3MzYxODA2MTQ3Nw.Gfs-tu.QP_yvc0aqe9vZPWhV6AjDZHWmK6jFR9naBD3L0'
}
#current=os.path.getsize('C:\\Users\\chotu\\Desktop\\stocks\\o.txt')
for i in range(10000000):
    os.system('curl https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/main/data/domains.txt -o o.txt')
    with open("C:\\Users\\chotu\\Desktop\\stocks\\o.txt",'r') as file1,open("C:\\Users\\chotu\\Desktop\\stocks\\new.txt",'r') as file2:
        diff=difflib.unified_diff(file1.readlines(),file2.readlines(),lineterm='')
        for line in diff:
            print(line,datetime.now())
            time=datetime.now()
            line=line+""+str(time)
            payload = {'content':line}
            r = requests.post("https://discord.com/api/v9/channels/1203177915752251435/messages", 
                    data=payload, headers=header)

    time.sleep(300)
    file1=file2
    #new=os.path.getsize('C:\\Users\\chotu\\Desktop\\stocks\\o.txt')
    #if new > current:
        #current=new
        #os.system('curl -d "new added check now" ntfy.sh/bbrsmend')
