import time
import subprocess
import sys
from tqdm import tqdm

def check_for_update() -> bool:
    for i in tqdm(range(100), desc="Checking for Update"):
        time.sleep(0.01)
    return True

def install_update() -> bool:
    for i in tqdm(range(100), desc="Updating Application"):
        time.sleep(0.01)
    return True

def launch_time_clock() -> None:
    subprocess.run([sys.executable, "time_clock/app.py"])

if __name__ == '__main__':
    check_for_update()
    install_update()
    launch_time_clock()