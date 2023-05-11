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


    def create_report_file(self, folder_path: str, file_with_path: str, execution_time: str):
        """ `+`
        `Type:` Procedure
        `Description:` creates a txt file
        :param:`path:` path where you save the file
        :param:`file_with_path:` file that stores the path to the settings
        :param:`execution_time:` time at which the test is performed
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
        self.__create_date_section(content_list, execution_time)
        self.__create_component_section(content_list)
        
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
            card_to_make_tuples = self.data.get_tuples(
                "SELECT (w.NbUnitsToDo div wrm.NbUnitsPerWork) AS carte FROM workorders w JOIN workorderrecipemachines wrm ON w.IdWorkOrder = wrm.IdWorkOrder WHERE w.Name = ?",
                [self.folder_name]
            )
            
            result = card_to_make_tuples[0][0]
            if result == card_to_make:
                content_list.append("-> Nombre de cartes à produire => OK")
                content_list.append(f"   - Valeur obtenue : {result}")
                content_list.append(f"   - Valeur expectée : {card_to_make}")
            else:
                content_list.append("-> Nombre de cartes à produire => NOK")
                content_list.append(f"   - Valeur obtenue : {result}")
                content_list.append(f"   - Valeur expectée : {card_to_make}")
        except Exception as e:
            content_list.append(f"==> [ERREUR] Nombre de cartes à produire => {e}")

        content_list.append(" ")
        
        # verification of the number of cards passed through the machine
        try:
            # get the value in the database
            card_tuples = self.data.get_tuples(
                "SELECT COUNT(*) FROM (workorders wo JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder) JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine WHERE wo.Name = ?",
                [self.folder_name]
            )
            
            result = card_tuples[0][0]
            if result == card_to_make:
                content_list.append("-> Nombre de cartes passées dans la machine => OK")
                content_list.append(f"   - Valeur obtenue : {result}")
                content_list.append(f"   - Valeur expectée : {card_to_make}")
            else:
                content_list.append("-> Nombre de cartes passées dans la machine => NOK")
                content_list.append(f"   - Valeur obtenue : {result}")
                content_list.append(f"   - Valeur expectée : {card_to_make}")
        except Exception as e:
            content_list.append(f"==> [ERREUR] Nombre de cartes passées dans la machine => {e}")

        content_list.append(" ")

        # verification of the number of fully produced cards
        try:
            # get the value in the database
            card_made_tuples = self.data.get_tuples(
                "SELECT COUNT(*) FROM (workorders wo JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder) JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine WHERE w.DateEnd != '' AND wo.Name = ?",
                [self.folder_name]
            )
            
            result = card_made_tuples[0][0]
            if result == card_to_make:
                content_list.append("-> Nombre de cartes produites entièrement => OK")
                content_list.append(f"   - Valeur obtenue : {result}")
                content_list.append(f"   - Valeur expectée : {card_to_make}")
            else:
                content_list.append("-> Nombre de cartes produites entièrement => NOK")
                content_list.append(f"   - Valeur obtenue : {result}")
                content_list.append(f"   - Valeur expectée : {card_to_make}")
        except Exception as e:
            content_list.append(f"==> [ERREUR] Nombre de cartes produites entièrement => {e}")

        content_list.append(" ")

        # verification of the result status of the cards
        try:
            # get the value in the database
            status_tuples = self.data.get_tuples(
                "SELECT w.Result FROM (workorders wo JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder) JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine WHERE wo.Name = ?",
                [self.folder_name]
            )

            content_list.append("-> Status Result")
            expected_value = "0"
            
            # for each card we look at its status
            for i, row in enumerate(status_tuples):
                # card status
                value = row[0]

                content_list.append(f"  => Carte N°{i+1}")

                if value == expected_value:
                    content_list.append("       -> Status Result => OK")
                    content_list.append(f"          - Valeur obtenue : {value}")
                    content_list.append(f"          - Valeur expectée : {expected_value}")
                else:
                    content_list.append("       -> Status Result => NOK")
                    content_list.append(f"          - Valeur obtenue : {value}")
                    content_list.append(f"          - Valeur expectée : {expected_value}")
        except Exception as e:
            content_list.append(f"==> [ERREUR] Status Result => {e}")

        content_list.append(" ")


    def __create_date_section(self, content_list: list, execution_time: str):
        """ `-`
        `Type:` Procedure
        `Description:` write in the report file the tests in the date section
        :param:`content_list:` file content
        :param:`execution_time:` time at which the test is performed
        """

        content_list.append("-------------------- Date --------------------\n")

        # verification of the consistency of the creation date
        try:
            # get the value in the database
            tuples = self.data.get_tuples(
                "SELECT DateCreation FROM workorders WHERE NAME = ?",
                [self.folder_name]
            )
            
            # dates in string
            date_result = tuples[0][0]

            date1 = datetime.strptime(date_result, "%Y-%m-%d %H:%M:%S.%f")
            date2 = datetime.strptime(execution_time, "%Y-%m-%d_%Hh%Mm%Ss")
    
            # calculate the difference between the two dates and define the tolerance at 2 minutes
            diff = abs(date1 - date2)
            tolerance = timedelta(minutes=1)

            if diff <= tolerance:
                content_list.append("-> Date de création => OK")
                content_list.append(f"   - Valeur obtenue : {date1}")
                content_list.append(f"   - Valeur expectée : {date2}")
            else:
                content_list.append("-> Date de création => NOK")
                content_list.append(f"   - Valeur obtenue : {date1}")
                content_list.append(f"   - Valeur expectée : {date2}")
        except Exception as e:
            content_list.append(f"==> [ERREUR] Date de création => {e}")

        content_list.append(" ")


    def __create_component_section(self, content_list: list):
        """ `-`
        `Type:` Procedure
        `Description:` write in the report file the tests in the component section
        :param:`content_list:` file content
        """

        content_list.append("-------------------- Composant --------------------\n")

        # verification of the number of components installed per card
        try:
            # get the values in the database
            # number of components per card
            nb_components_tuples = self.data.get_tuples(
                "SELECT worm.NbUnitsPerWork, worm.NbComponentsPerUnit FROM (workorders wo JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder) WHERE wo.Name = ?",
                [self.folder_name]
            )
            
            nb_unit_per_work = nb_components_tuples[0][0]
            nb_components_per_unit = nb_components_tuples[0][1]
            nb_components_per_card_expected = int(nb_unit_per_work) * int(nb_components_per_unit)

            # id of the cards
            id_work_tuples = self.data.get_tuples(
                "SELECT w.IdWork FROM (workorders wo JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder) JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine WHERE wo.Name = ?",
                [self.folder_name]
            )

            flat_list = [element for sub_list in id_work_tuples for element in sub_list]

            content_list.append("-> Nombre de composants posés par carte")

            # for each card we check the number of components placed
            for i, id_work in enumerate(flat_list):

                content_list.append(f"  => Carte N°{i+1}")

                # number of components installed for this card
                nb_components_installed_tuples = self.data.get_tuples(
                    "SELECT COUNT(*) FROM workorders wo JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine JOIN activities a ON w.IdWork = a.IdWork JOIN components c ON c.IdActivity = a.IdActivity WHERE wo.Name = ? AND w.IdWork = ?",
                    [self.folder_name, id_work]
                )

                installed_components = nb_components_installed_tuples[0][0]

                if int(installed_components) == nb_components_per_card_expected:
                    content_list.append("       -> Nombre de composants posés par carte => OK")
                    content_list.append(f"          - Valeur obtenue : {installed_components}")
                    content_list.append(f"          - Valeur expectée : {nb_components_per_card_expected}")
                else:
                    content_list.append("       -> Nombre de composants posés par carte => NOK")
                    content_list.append(f"          - Valeur obtenue : {installed_components}")
                    content_list.append(f"          - Valeur expectée : {nb_components_per_card_expected}")
        except Exception as e:
            content_list.append(f"==> [ERREUR] Nombre de composants posés par carte => {e}")

        content_list.append(" ")