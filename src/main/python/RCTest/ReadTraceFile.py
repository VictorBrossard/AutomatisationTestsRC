# Author        : Victor BROSSARD
# Description   : Class that reads the trace file and launches the right files for the test

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os
import shutil

from FilesManagement.Files.ManipulationSettingsFile import ManipulationSettingsFile

from FilesManagement.Folders.ManageFolders import CONSTANT_TESTS_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------

class ReadTraceFile(object):
    """ `+`
    :class:`ReadTraceFile` reads the trace file and launches the right files for the test
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        self.trace_path = ManipulationSettingsFile().get_line(8)


    def find_trace(self, trace_list: list):
        """ ``
        `Type:`
        `Description:`
        """

        path_trace_file = f"{self.trace_path}\\ieee001.TRC"
        path_copy_trace_file = f"{CONSTANT_TESTS_FOLDER_PATH}\\ieee001.TRC"

        shutil.copy(path_trace_file, CONSTANT_TESTS_FOLDER_PATH)

        trace_file = open(path_copy_trace_file, "rb")

        print(trace_list)
        trace_file.seek(0, os.SEEK_END)
        trace_file.seek(-2, os.SEEK_CUR)
        trace_file.seek(-2, os.SEEK_CUR)
        print(trace_file.readline().decode().strip())

        trace_file.close()

        os.remove(path_copy_trace_file)

