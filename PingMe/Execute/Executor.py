import time
import subprocess
import sys

class Executor():

    def __init__(self, args, reporter,
            stin = sys.stdin, stout = sys.stdout, sterr = sys.stderr):
        self._stin = stin
        self._stout = stout
        self._sterr = sterr
        self._execute_cmd = self._BuildCmd(args)
        self._reporter = reporter
        self.Execute()


    def _BuildCmd(self, args):
        """
        Builds a cmd from all of the args for the executable passed in
        """
        arg_list = [args[0]]
        arg_string = ""
        for i in range(len(args) - 1):
            arg_string += args[i + 1] + " "

        arg_string = arg_string[:-1]
        if arg_string is not "":
            arg_list.append(arg_string)
        return arg_list

    def Execute(self):
        """
        Runs the cmd
        """
        start_time = time.time()
        try:
            r_code = subprocess.call(self._execute_cmd,
                    stdin= self._stin,
                    stdout = self._stout,
                    stderr= self._sterr)
        except FileNotFoundError:
            print(self._execute_cmd[0] + " was not found, could not run process")
            r_code = -1
        end_time = time.time()
        total_time = end_time - start_time
        self._reporter.Report(rcode = r_code, ttime = total_time)
