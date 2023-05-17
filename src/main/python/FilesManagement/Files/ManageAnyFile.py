# Author        : Victor BROSSARD
# Description   : Class that manages any file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os

#-----------------------------------------------------------------------------------------------------

class ManageAnyFile(object):
    """ `+`
    :class:`ManageAnyFile` manages any file
    """
    
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        pass


    def create_file(self, path: str, file_name: str, line_list: list):
        """ `+`
        `Type:` Procedure
        `Description:` creates a txt file
        :param:`path:` path where you save the file
        :param:`file_name:` file name
        :param:`line_list:` line to write in the file
        """

        if os.path.exists(f"{path}\\{file_name}"):
            return

        # Creation of the file 
        os.chdir(path) # Change the current working directory by giving the path
        subprocess.run(['type', 'nul', '>', file_name], shell=True)                     

        # Save the values in the file we have created
        os.chdir(path)
        file_path = open(file_name, 'w') # Opening the file in write mode ('w')

        if line_list != []:
            for line in line_list:
                file_path.write(f"{line}\n")

        file_path.close()


    def delete_file(self, path: str):
        """ `+`
        `Type:` Procedure
        `Description:` delete the file
        :param:`path:` path of the file
        """

        os.remove(path)

    
    def get_file_lines(self, file_path: str) -> list[str]:
        """ `+`
        `Type:` Function
        `Description:` retrieves the values from the file
        :param:`file_path:` file path
        `Return:` lines of the files
        """

        try:
            fil = open(file_path, 'r')
            lines = fil.readlines()
            fil.close()
        except Exception as e:
            print(f"[ERREUR] {e}")
            return []
        
        lines_without_whitespace = [s.strip() for s in lines]
        
        return lines_without_whitespace