# Author        : Victor BROSSARD
# Description   : Class that manages report file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import os

from datetime import timedelta
from datetime import datetime

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
        self.folder_name = os.path.basename(folder_path)

        # will retrieve the values of the settings used for the report
        settings = self.__get_settings_values(file_with_path)

        if settings == []: return

        # future file content
        content_list = []
        content_list.append(f"Nom : {settings[0]}\n")

        self.__create_card_section(content_list, settings[1])
        self.__create_date_section(content_list)
        
        # report creation
        self.create_file(folder_path, "report.txt", content_list)


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
    

    def __create_card_section(self, content_list: list, card_to_make: str):
        """ `-`
        `Type:` Procedure
        `Description:` write in the report file the tests in the card section
        :param:`content_list:` file content
        :param:`card_to_made:` card to make
        """

        content_list.append("-------------------- Carte --------------------\n")

        # verification of the number of cards to be produced
        try:
            # get the value in the database
            tuples = self.data.get_tuples(
                "SELECT (w.NbUnitsToDo div wrm.NbUnitsPerWork) AS carte FROM workorders w JOIN workorderrecipemachines wrm ON w.IdWorkOrder = wrm.IdWorkOrder WHERE w.Name = ?",
                [self.folder_name]
            )
            
            result = tuples[0][0]
            if result == card_to_make:
                content_list.append("-> Nombre de cartes à produire => OK")
            else:
                content_list.append("-> Nombre de cartes à produire => NOK")
        except Exception:
            content_list.append("-> Nombre de cartes à produire => ERREUR")
        
        # verification of the number of cards produced
        try:
            # get the value in the database
            tuples = self.data.get_tuples(
                "SELECT COUNT(*) FROM (workorders wo JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder) JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine WHERE wo.Name = ?",
                [self.folder_name]
            )
            
            result = tuples[0][0]
            if result == card_to_make:
                content_list.append("-> Nombre de cartes produite => OK")
            else:
                content_list.append("-> Nombre de cartes produite => NOK")
        except Exception:
            content_list.append("-> Nombre de cartes produite => ERREUR")

        content_list.append(" ")


    def __create_date_section(self, content_list: list):
        """ `-`
        `Type:` Procedure
        `Description:` write in the report file the tests in the date section
        :param:`content_list:` file content
        """

        content_list.append("-------------------- Date --------------------\n")

        # 
        try:
            # get the value in the database
            tuples = self.data.get_tuples(
                "SELECT DateCreation FROM workorders WHERE NAME = ?",
                [self.folder_name]
            )
            
            # dates in string
            date_result = tuples[0][0]
            separate_test_date = self.folder_name.split("_")
            date_test = f"{separate_test_date[1]}_{separate_test_date[2]}"

            date1 = datetime.strptime(date_result, "%Y-%m-%d %H:%M:%S.%f")
            date2 = datetime.strptime(date_test, "%Y-%m-%d_%Hh%Mm%Ss")
    
            # calculate the difference between the two dates and define the tolerance at 2 minutes
            diff = abs(date1 - date2)
            tolerance = timedelta(minutes=2)

            if diff <= tolerance:
                content_list.append("-> Date de création => OK")
            else:
                content_list.append("-> Date de création => NOK")
        except Exception:
            content_list.append("-> Date de création => ERREUR")

        content_list.append(" ")