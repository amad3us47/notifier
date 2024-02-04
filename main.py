import os
import time
current=os.path.size('/home/runner/work/automation/automation/new.txt')
os.system('curl https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/main/data/domains.txt -o o.txt')
new=os.path.getsize('/home/runner/work/automation/automation/o.txt')
if new > current:
        current=new
        os.system('curl -d "new added check now" ntfy.sh/bbrsmend')
else:
        current=new
