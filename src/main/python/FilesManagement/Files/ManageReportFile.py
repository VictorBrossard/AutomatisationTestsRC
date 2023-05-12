# Author        : Victor BROSSARD
# Description   : Class that manages report file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import os

from FilesManagement.Files.ManageAnyFile import ManageAnyFile

from Database.Database import Database

from GraphicInterface.MessageBox import MessageBox

from RCTest.CheckTest import CheckTest

#-----------------------------------------------------------------------------------------------------

class ManageReportFile(ManageAnyFile):
    """ `+`
    :class:`ManageReportFile` manages report file
    """
    
    def __init__(self, database: Database, folder_path: str, file_with_path: str, execution_time: str):
        """ `-`
        `Type:` Constructor
        :param:`database:` object that manages the interaction with the database
        :param:`path:` path where you save the file
        :param:`file_with_path:` file that stores the path to the settings
        :param:`execution_time:` time at which the test is performed
        """

        self.data = database
        self.folder_path = folder_path
        self.file_with_path = file_with_path
        self.execution_time = execution_time
        self.test_name = os.path.basename(folder_path) # name of the file which is also the name of the test
        self.check_test = CheckTest(self.data, self.test_name)
        self.content_list = [] # future file content


    def create_report_file(self):
        """ `+`
        `Type:` Procedure
        `Description:` execute the private function __create_report_file
        """

        self.__create_report_file(self.folder_path, self.file_with_path, self.execution_time)


    def __create_report_file(self, folder_path: str, file_with_path: str, execution_time: str):
        """ `-`
        `Type:` Procedure
        `Description:` creates a txt file
        :param:`path:` path where you save the file
        :param:`file_with_path:` file that stores the path to the settings
        :param:`execution_time:` time at which the test is performed
        """

        # will retrieve the values of the settings used for the report
        settings = self.__get_settings_values(file_with_path)

        if settings == []: return

        self.content_list.append(f"Nom : {settings[0]}\n")

        self.__create_card_section(settings[1])
        self.__create_date_section(execution_time)
        self.__create_component_section()
        
        # report creation
        self.create_file(folder_path, "report.txt", self.content_list)


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
    

    def __create_card_section(self, card_to_make: str):
        """ `-`
        `Type:` Procedure
        `Description:` write in the report file the tests in the card section
        :param:`card_to_made:` card to make
        """

        self.content_list.append("-------------------- Carte --------------------\n")

        # verification of the number of cards to be produced
        self.check_test.nb_cards_to_be_produced(self.content_list, card_to_make)
        
        # verification of the number of cards passed through the machine
        self.check_test.nb_cards_passed_machine(self.content_list, card_to_make)

        # verification of the number of fully produced cards
        self.check_test.nb_produced_cards(self.content_list, card_to_make)

        # verification of the result status of the cards
        self.check_test.cards_result_status(self.content_list)


    def __create_date_section(self, execution_time: str):
        """ `-`
        `Type:` Procedure
        `Description:` write in the report file the tests in the date section
        :param:`content_list:` file content
        :param:`execution_time:` time at which the test is performed
        """

        self.content_list.append("-------------------- Date --------------------\n")

        # verification of the consistency of the creation date
        self.check_test.creation_date_constency(self.content_list, execution_time)

        # verification of the consistency of the begin date in workorderactivationhistory
        self.check_test.begin_date_constency(self.content_list, execution_time)

        # checking the consistency of the start and end dates of a card
        self.check_test.check_start_end_date_card(self.content_list)


    def __create_component_section(self):
        """ `-`
        `Type:` Procedure
        `Description:` write in the report file the tests in the component section
        """

        self.content_list.append("-------------------- Composant --------------------\n")

        # verification of the number of components installed per card
        self.check_test.nb_components_installed(self.content_list)