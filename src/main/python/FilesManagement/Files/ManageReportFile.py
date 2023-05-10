# Author        : Victor BROSSARD
# Description   : Class that manages report file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os

from FilesManagement.Files.ManageAnyFile import ManageAnyFile

from Database.Database import Database

from GraphicInterface.MessageBox import MessageBox

#-----------------------------------------------------------------------------------------------------

class ManageReportFile(ManageAnyFile):
    """ `+`
    :class:`ManageReportFile` manages report file
    """
    
    def __init__(self, database: Database):
        """ `-`
        `Type:` Constructor
        """

        self.data = database


    def create_report_file(self, folder_path: str, file_with_path: str):
        """ `+`
        `Type:` Procedure
        `Description:` creates a txt file
        :param:`path:` path where you save the file
        :param:`file_with_path:` file that stores the path to the settings
        """

        # retrieve the folder name
        folder_name = os.path.basename(folder_path)

        # will retrieve the values of the settings used for the report
        settings = self.__get_settings_values(file_with_path)

        if settings == []: return

        # future file content
        content_list = []
        content_list.append(f"Nom : {settings[0]}\n")

        # verification of the number of cards to be produced
        if self.__compare(
            "SELECT (w.NbUnitsToDo div wrm.NbUnitsPerWork) AS carte FROM workorders w JOIN workorderrecipemachines wrm ON w.IdWorkOrder = wrm.IdWorkOrder WHERE w.Name = ?",
            [folder_name],
            settings[1]
        ):
            content_list.append("-> Nombre de cartes à produire : OK")
        else:
            content_list.append("-> Nombre de cartes à produire : NOK")
        
        # report creation
        self.create_file(folder_path, "report.txt", content_list)


    def __compare(self, command: str, variable_list: list, value: str):
        """ `-`
        `Type:` Function
        `Description:` compares a given value to the value returned by the SQL command (the command must return absolutely only one value) 
        :param:`command:` sql command
        :param:`variable_list:` list of variables in the command
        :param:`value:` value to compare
        `Return:` bool
        """

        try:
            # get the value in the database
            result = self.data.get_tuples(command, variable_list)

            if len(result) != 1:
                return False
            
            first = result[0][0]
        except Exception:
            return False

        # compare
        return value == first


    def __get_settings_values(self, file_with_path: str):
        """ `-`
        `Type:` Function
        `Description:` retrieves the values from the settings file
        :param:`file_with_path:` file that stores the path to the settings
        `Return:` settings values list
        """

        # get the path in the file
        try:
            fil = open(file_with_path, 'r')
            path_line = fil.readlines()[0].rstrip()
            fil.close()
        except Exception as e:
            MessageBox("ERREUR Fichier", f"[ERREUR] {e}").mainloop()
            return []
        
        # name of the folder where it is
        test_name = os.path.basename(path_line)
        
        # content recovery
        try:
            fil = open(f"{path_line}\\{test_name}_settings.txt", 'r')
            settings_values = fil.readlines()
            fil.close()
        except Exception as e:
            MessageBox("ERREUR Fichier", f"[ERREUR] {e}").mainloop()
            return []
        
        settings_values = [s.strip() for s in settings_values]

        return settings_values