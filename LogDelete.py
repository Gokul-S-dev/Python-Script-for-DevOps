import os
import time

LOG_DIRECTORY = "/var/log"
DAYS_OLD = 30

current_time = time.time()

for filename in os.listdir(LOG_DIRECTORY):
    file_path = os.path.join(LOG_DIRECTORY, filename)

    if os.path.isfile(file_path) and filename.endswith(".log"):
        file_age = current_time - os.path.getmtime(file_path)

        if file_age > DAYS_OLD * 24 * 60 * 60:
            os.remove(file_path)
            print(f"Deleted log file: {file_path}")

print("Log deletion process completed.")