import os
import hashlib


class FileMonitor:
    def __init__(self, path):
        self.path = path
        self.state = False
        self.files = os.listdir(self.path)
        self.upd_files = []

    def start(self):
        self.upd_files = os.listdir(self.path)
        if self.upd_files:
            self.check_dir()
            self.check_file()
            self.files = self.upd_files

    def check_dir(self):
        dif_files = list(set(self.files) - set(self.upd_files))
        add_files = list(set(self.upd_files) - set(self.files))
        if dif_files:
            print("Deleted: ", dif_files)
        if add_files:
            print("Added: ", add_files)

    def get_file_hash(self, file_path):
        if os.path.exists(file_path) is False:
            return None
        else:
            md5 = hashlib.md5()
            file = open(file_path)
            for line in file:
                md5.update(line)
                file.close()
            return md5.hexdigest()

    def check_file(self):
        for file in self.files:
            print(self.get_file_hash(file))
