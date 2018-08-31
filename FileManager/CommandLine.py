import threading
from FileMonitor import FileMonitor


class CommandLine(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.__file_monitors = dict()
        self.__check_status = False

    def __help(self):
        pass

    def __stop(self, user_command):
        self.__check_status = False

    @staticmethod
    def __file_monitor_doesnt_exist_error_message(title):
        print('A monitor', title, 'does not exist.\n')

    @staticmethod
    def __command_error_message():
        print("Wrong command. Use 'help' to see the list of commands and theirs usage.\n")

    def __stop_monitor(self, title):
        self.__file_monitors[title].stop()
        print('File monitor', title, 'stopped!\n')

    def __create_file_monitor(self, user_command):
        if len(user_command) == 2:
            self.__file_monitors[user_command[0]] = FileMonitor(user_command[0], user_command[1])
            print('File monitor', user_command[0], 'at path', user_command[1], 'created!\n')
            return True
        return False

    def __remove_file_monitor(self, user_command):
        if len(user_command) == 1:
            try:
                if self.__file_monitors[user_command[0]].check_status:
                    self.__stop_monitor(user_command[0])
                print('File monitor ', self.__file_monitors.pop(user_command[0]).title, 'removed!\n')
                return True
            except KeyError:
                self.__file_monitor_doesnt_exist_error_message(user_command[0])
        return False

    def __start_file_monitor(self, user_command):
        if len(user_command) == 1:
            try:
                if not self.__file_monitors[user_command[0]].check_status:
                    self.__file_monitors[user_command[0]].start()
                    print('File monitor', user_command[0], 'started!\n')
                else:
                    print('File monitor', user_command[0], 'is now running!\n')
                return True
            except KeyError:
                self.__file_monitor_doesnt_exist_error_message(user_command[0])
        return False

    def __stop_file_monitor(self, user_command):
        if len(user_command) == 1:
            try:
                if self.__file_monitors[user_command[0]].check_status:
                    self.__stop_monitor(user_command[0])
                else:
                    print('File monitor', user_command[0], 'not running now!\n')
                return True
            except KeyError:
                self.__file_monitor_doesnt_exist_error_message(user_command[0])
        return False

    def __check_list_of_file_monitors(self, user_command):
        if len(user_command) == 0:
            print('Name:\tPath:')
            for file_monitor_key in self.__file_monitors:
                print(file_monitor_key, '\t', self.__file_monitors[file_monitor_key].folder_path_str)
                print()
            return True
        return False

    def run(self):
        self.__check_status = True
        commands = {'create-file-monitor': self.__create_file_monitor,
                    'remove-file-monitor': self.__remove_file_monitor,
                    'start-file-monitor': self.__start_file_monitor,
                    'stop-file-monitor': self.__stop_file_monitor,
                    'list': self.__check_list_of_file_monitors,
                    'help': self.__help,
                    'stop': self.__stop
                    }
        while self.__check_status:
            try:
                user_command = input().split()
                if commands[user_command[0]](user_command[1:]):
                    continue
                self.__command_error_message()
            except ValueError:
                self.__command_error_message()
