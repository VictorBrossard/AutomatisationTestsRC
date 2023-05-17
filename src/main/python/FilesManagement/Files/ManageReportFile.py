# Author        : Victor BROSSARD
# Description   : Class that manages report file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import os

from FilesManagement.Files.ManageAnyFile import ManageAnyFile

from Database.Database import Database

from RCTest.CheckTest import CheckTest

#-----------------------------------------------------------------------------------------------------

class ManageReportFile(ManageAnyFile):
    """ `+`
    :class:`ManageReportFile` manages report file
    """
    
    def __init__(self, database: Database, report_folder_path: str, test_folder_path: str, time_create_folder: str, start_test_time: str, index: str):
        """ `-`
        `Type:` Constructor
        :param:`database:` object that manages the interaction with the database
        :param:`report_folder_path:` path where you save the file
        :param:`test_folder_path:` path of the test file to be analyzed
        :param:`time_create_folder:` time the folder is created
        :param:`start_time:` time when you press start
        :param:`index:` test index
        """

        self.data = database
        self.report_folder_path = report_folder_path
        self.test_folder_path = test_folder_path
        self.time_create_folder = time_create_folder
        self.start_time = start_test_time
        self.index = index
        
        self.test_name = os.path.basename(report_folder_path) # name of the file which is also the name of the test
        self.check_test = CheckTest(self.data, self.test_name)
        self.content_list = [] # future file content


    def create_report_file(self):
        """ `+`
        `Type:` Procedure
        `Description:` execute the private function __create_report_file
        """

        self.__create_report_file(self.report_folder_path, self.test_folder_path)


    def __create_report_file(self, report_folder_path: str, test_folder_path: str):
        """ `-`
        `Type:` Procedure
        `Description:` creates a txt file
        :param:`report_folder_path:` path where you save the file
        :param:`test_folder_path:` path of the test file to be analyzed
        """

        # will retrieve the values of the settings used for the report
        settings_file_name = f"{os.path.basename(self.test_folder_path)}_settings.txt"
        settings = self.get_file_lines(f"{test_folder_path}\\{settings_file_name}")
        temp_test_settings = self.get_file_lines(f"{test_folder_path}\\test_{self.index}.txt")

        if settings == []: return

        self.content_list.append(f"Nom : {settings[0]}\n")
        self.content_list.append(f"Type de test : {settings[1]}\n")
        self.content_list.append(f"Initialisation de la machine : {temp_test_settings[2]}\n")
        self.content_list.append(f"Programme : {temp_test_settings[3]}\n")

        self.__create_card_section(temp_test_settings[0])
        self.__create_date_section()
        self.__create_component_section()
        
        # report creation
        self.create_file(report_folder_path, "report.txt", self.content_list)
    

    def __create_card_section(self, card_to_make: str):
        """ `-`
        `Type:` Procedure
        `Description:` write in the report file the tests in the card section
        :param:`card_to_made:` card to make
        """

        self.content_list.append("------------------------------------------------------------ Carte ------------------------------------------------------------\n")

        # verification of the number of cards to be produced
        self.check_test.nb_cards_to_be_produced(self.content_list, card_to_make)
        
        # verification of the number of cards passed through the machine
        self.check_test.nb_cards_passed_machine(self.content_list, card_to_make)

        # verification of the number of fully produced cards
        self.check_test.nb_produced_cards(self.content_list, card_to_make)

        # verification of the result status of the cards
        self.check_test.cards_result_status(self.content_list)


    def __create_date_section(self):
        """ `-`
        `Type:` Procedure
        `Description:` write in the report file the tests in the date section
        """

        self.content_list.append("------------------------------------------------------------ Date ------------------------------------------------------------\n")

        # verification of the consistency of the creation date
        self.check_test.creation_date_constency(self.content_list, self.time_create_folder)

        # verification of the consistency of the begin date in workorderactivationhistory
        self.check_test.test_begin_date_constency(self.content_list, self.time_create_folder)

        #
        self.check_test.check_date_begin_equal_start(self.content_list, self.start_time)

        # checking the consistency of the start and end dates of a card
        self.check_test.check_start_end_date_card(self.content_list)


    def __create_component_section(self):
        """ `-`
        `Type:` Procedure
        `Description:` write in the report file the tests in the component section
        """

        self.content_list.append("------------------------------------------------------------ Composant ------------------------------------------------------------\n")

        # verification of the number of components installed per card
        self.check_test.nb_components_installed(self.content_list)