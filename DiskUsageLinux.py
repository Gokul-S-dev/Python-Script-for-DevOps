import shutil
import socket
from datetime import datetime

THRESHOLD = 80 # Set the threshold for disk usage percentage

def check_disk_usage():
    total, used, free = shutil.disk_usage("/")

    usage_percentage = ( used / total) * 100

    print(f"\n Server: {socket.gethostname()}")
    print(f"Time : {datetime.now()}")
    print(f"Total Disk Space: {total // (1024 ** 3)} GB")
    print(f"Used Disk Space: {used // (1024 ** 3)} GB")
    print(f"Used Space : {free // (1024**3)}")
    print(f"Usage Percentage: {usage_percentage:.2f}%")

    if usage_percentage > THRESHOLD:
        print(f"\n Warning: Disk usage is above {THRESHOLD}%! Please take action to free up space.")
    else:
        print(f"\n Disk usage is within acceptable limits.")

if __name__ == "__main__":
    check_disk_usage()
