# -*- coding: utf-8 -*-

import subprocess as sub
import os


class PFSProcess(object):
    def __init__(self, submodule, path, cmd, counter, output_filter=""):
        self.__submodule = submodule
        self.__path = path
        self.__cmd = cmd
        self.__counter = counter
        self.__output_filter = output_filter
        self.__output = None
        self.__p = None

    def run(self):
        self.__output = "\n\n" + self.__submodule + "\n"
        # self.__output = sub.check_output(self.__cmd)
        self.__p = sub.Popen(self.__cmd, stdout=sub.PIPE, stderr=sub.PIPE, shell=True,
                             cwd=os.path.join(self.__path, self.__submodule))

        if self.__output_filter == "":
            self.__output += self.__p.communicate()[0].decode('utf-8')  # stdoutdata
        else:
            if str(self.__p.communicate()[0].decode('utf-8')).find(self.__output_filter) != -1:
                self.__output += self.__p.communicate()[0].decode('utf-8')

        if self.__p.communicate()[1]:  # stderrdata
            self.__output += self.__p.communicate()[1].decode('utf-8')

        self.__output += str(self.__counter.increment_value())
        print(self.__output)
