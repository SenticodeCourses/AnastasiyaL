import os
import time
import threading


class FileMonitor(threading.Thread):

    def __init__(self, title, folder_path):
        threading.Thread.__init__(self)
        self.title = title
        self.folder_path_str = folder_path
        self.previous_folder_condition = None
        self.check_status = False

    def __check_files(self):
        current_folder_condition = set(os.listdir('.'))
        deleted_files = self.previous_folder_condition.difference(current_folder_condition)
        new_files = current_folder_condition.difference(self.previous_folder_condition)
        self.previous_folder_condition = current_folder_condition
        if len(new_files) > 0:
            print(self.title, 'Added files:')
            for file in new_files:
                print(file, '\n')
        if len(deleted_files) > 0:
            print(self.title, 'Deleted files:')
            for file in deleted_files:
                print(file, '\n')

    def run(self):
        os.chdir(self.folder_path_str)
        self.previous_folder_condition = set(os.listdir('.'))
        self.check_status = True
        while self.check_status:
            time.sleep(0.3)
            self.__check_files()

    def stop(self):
        self.check_status = False