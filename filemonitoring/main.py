from filemonitor import FileMonitor
import time

fm = FileMonitor('some_folder')
while True:
    fm.start()
    time.sleep(5)
