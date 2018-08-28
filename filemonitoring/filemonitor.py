import os


class FileMonitor:
    def __init__(self, path):
        self.path = path
        self.state = False
        self.files = os.listdir(self.path)
        self.upd_files = []

    def start(self):
        self.upd_files = os.listdir(self.path)
        if self.upd_files:
            self.check()
            self.files = self.upd_files

    def check(self):
        dif_files = list(set(self.files) - set(self.upd_files))
        add_files = list(set(self.upd_files) - set(self.files))
        if dif_files:
            print("Deleted: ", dif_files)
        if add_files:
            print("Added: ", add_files)
