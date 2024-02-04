import os
import time
from pathlib import Path
path_current=Path('/home/runner/work/automation/automation/new.txt')
path_new=Path('/home/runner/work/automation/automation/o.txt')
current=os.path.getsize(path_current)
os.system('curl https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/main/data/domains.txt -o o.txt')
new=os.path.getsize(path_new)
if new > current:
        current=new
        os.system('curl -d "new added check now" ntfy.sh/bbrsmend')
else:
        current=new
