import datetime
import time
import os

def get_current_time():
    os.system('clear')
    now = datetime.datetime.now()
    print(now.strftime("%H:%M:%S"))
    time.sleep(1)
    get_current_time()

get_current_time()