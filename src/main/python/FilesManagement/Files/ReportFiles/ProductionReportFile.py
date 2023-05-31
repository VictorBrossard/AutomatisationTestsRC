# Author        : Victor BROSSARD
# Description   : Class that manages the creation of the production test report

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
from Database.Database import Database

from FilesManagement.Files.ManageReportFile import ManageReportFile

from RCTest.Tests.CheckProductionTest import CheckProductionTest

from Useful.AllConstant import CONSTANT_TEST_SETTINGS_FILE_NAME

#-----------------------------------------------------------------------------------------------------

class ProductionReportFile(ManageReportFile):
    """ `+`
    :class:`ProductionReportFile` manages the creation of the production test report
    """
    
    def __init__(self, database: Database, report_folder_path: str, test_folder_path: str):
        """ `-`
        `Type:` Constructor
        :param:`database:` object that manages the interaction with the database
        :param:`report_folder_path:` path where you save the file
        :param:`test_folder_path:` path of the test file to be analyzed
        """

        super().__init__(database, report_folder_path, test_folder_path)
        
        self.check_test = CheckProductionTest(self.data, self.test_name)


    def create_report_file_test(self, time_create_folder: str, start_test_time: str):
        """ `+`
        `Type:` Procedure
        `Description:` creates a txt report file for production test
        :param:`start_time:` time when you press start
        :param:`time_create_folder:` time the folder is created
        """

        # will retrieve the values of the settings used for the report
        settings = self.get_file_lines(f"{self.test_folder_path}\\{CONSTANT_TEST_SETTINGS_FILE_NAME}")

        if settings == []: return

        # overall status of all tests
        test_status_list = []

        # file header
        self.content_list.append(f"Type de test : {settings[0]}")
        self.content_list.append(f"Programme : {settings[3]}\n")

        # contains tests that are stored in a temporary list because we have to write the general status of the tests to the file first
        test_status_list.append(self.__create_card_section(settings[1]))
        test_status_list.append(self.__create_date_section(time_create_folder, start_test_time))
        test_status_list.append(self.__create_component_section())

        # general status of the tests
        global_status = "OK" if all(test_status_list) else "NOK"
        self.content_list.append(f"Status global : {global_status}\n")

        # entire contents of the file
        self.content_list = self.content_list + self.temp_content_list
        
        # report creation
        self.create_file(self.report_folder_path, "report.txt", self.content_list)
    

    def __create_card_section(self, card_to_make: str):
        """ `-`
        `Type:` Procedure
        `Description:` write in the report file the tests in the card section
        :param:`card_to_make:` card to make
        `Return:` status of the entire test
        """

        # overall status of all tests
        test_status_list = []

        self.temp_content_list.append("------------------------------------------------------------ Carte ------------------------------------------------------------\n")

        # verification of the number of cards to be produced
        test_status_list.append(self.check_test.nb_cards_to_be_produced(self.temp_content_list, card_to_make))
        
        # verification of the number of cards passed through the machine
        test_status_list.append(self.check_test.nb_cards_passed_machine(self.temp_content_list, card_to_make))

        # verification of the number of fully produced cards
        test_status_list.append(self.check_test.nb_produced_cards(self.temp_content_list, card_to_make))

        # verification of the result status of the cards
        test_status_list.append(self.check_test.cards_result_status(self.temp_content_list))

        return True if all(test_status_list) else False


    def __create_date_section(self, time_create_folder: str, start_test_time: str):
        """ `-`
        `Type:` Procedure
        `Description:` write in the report file the tests in the date section
        :param:`start_time:` time when you press start
        :param:`time_create_folder:` time the folder is created
        `Return:` status of the entire test
        """

        # overall status of all tests
        test_status_list = []

        self.temp_content_list.append("------------------------------------------------------------ Date ------------------------------------------------------------\n")

        # verification of the consistency of the creation date
        test_status_list.append(self.check_test.creation_date_constency(self.temp_content_list, time_create_folder))

        # verification of the consistency of the begin date in workorderactivationhistory
        test_status_list.append(self.check_test.test_begin_date_constency(self.temp_content_list, time_create_folder))

        # check that the production start date is equal to the time when you press the start button
        test_status_list.append(self.check_test.check_date_begin_equal_start_prod(self.temp_content_list, start_test_time))

        # checking the consistency of the start and end dates of a card
        test_status_list.append(self.check_test.check_start_end_date_card(self.temp_content_list))

        # verify if the start date of the card between start and end of the card before
        test_status_list.append(self.check_test.beginning_card_before_end_previous_card(self.temp_content_list))

        return True if all(test_status_list) else False


    def __create_component_section(self):
        """ `-`
        `Type:` Procedure
        `Description:` write in the report file the tests in the component section
        `Return:` status of the entire test
        """

        # overall status of all tests
        test_status_list = []

        self.temp_content_list.append("------------------------------------------------------------ Composant ------------------------------------------------------------\n")

        # verification of the number of components installed per card
        test_status_list.append(self.check_test.nb_components_installed(self.temp_content_list))

        return True if all(test_status_list) else False