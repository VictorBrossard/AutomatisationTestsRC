# Author        : Victor BROSSARD
# Description   : 

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
from Database.Database import Database

from datetime import timedelta
from datetime import datetime

#-----------------------------------------------------------------------------------------------------
# Initialization of constants
CONSTANT_FORMAT_DATES_DATABASE = "%Y-%m-%d %H:%M:%S.%f"
CONSTANT_SHORT_FORMAT_DATES_DATABASE = "%Y-%m-%d %H:%M:%S"

#-----------------------------------------------------------------------------------------------------

class CheckTest(object):
    """ `+`
    :class:`CheckTest` 
    """

    def __init__(self, database: Database, test_name: str):
        """ `-`
        `Type:` Constructor
        :param:`database:` object that manages the interaction with the database
        :param:`test_name:` 
        """

        self.data = database
        self.test_name = test_name


    ################################################################ Card section ################################################################


    def nb_cards_to_be_produced(self, content_list: list, card_to_make: str):
        """ `+`
        `Type:` Procedure
        `Description:` verification of the number of cards to be produced
        :param:`content_list:` file content
        :param:`card_to_made:` card to make
        """

        try:
            # get the value in the database
            card_to_make_tuples = self.data.get_tuples(
                """SELECT (w.NbUnitsToDo div wrm.NbUnitsPerWork) AS carte 
                FROM workorders w 
                JOIN workorderrecipemachines wrm ON w.IdWorkOrder = wrm.IdWorkOrder 
                WHERE w.Name = ?""",
                [self.test_name]
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


    def nb_cards_passed_machine(self, content_list: list, card_to_make: str):
        """ `+`
        `Type:` Procedure
        `Description:` verification of the number of cards passed through the machine
        :param:`content_list:` file content
        :param:`card_to_made:` card to make
        """

        try:
            # get the value in the database
            card_tuples = self.data.get_tuples(
                """SELECT COUNT(*) 
                FROM workorders wo 
                JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder 
                JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine 
                WHERE wo.Name = ?""",
                [self.test_name]
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


    def nb_produced_cards(self, content_list: list, card_to_make: str):
        """ `+`
        `Type:` Procedure
        `Description:` verification of the number of fully produced cards
        :param:`content_list:` file content
        :param:`card_to_made:` card to make
        """

        try:
            # get the value in the database
            card_made_tuples = self.data.get_tuples(
                """SELECT COUNT(*) 
                FROM workorders wo 
                JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder 
                JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine 
                WHERE w.DateEnd != '' AND wo.Name = ?""",
                [self.test_name]
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


    def cards_result_status(self, content_list: list):
        """ `+`
        `Type:` Procedure
        `Description:` verification of the result status of the cards
        :param:`content_list:` file content
        """

        try:
            # get the value in the database
            status_tuples = self.data.get_tuples(
                """SELECT w.Result 
                FROM workorders wo 
                JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder 
                JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine 
                WHERE wo.Name = ?""",
                [self.test_name]
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


    ################################################################ Date section ################################################################


    def creation_date_constency(self, content_list : list, folder_creation_time: str):
        """ `+`
        `Type:` Procedure
        `Description:` verification of the consistency of the creation date
        :param:`content_list:` file content
        :param:`folder_creation_time:` time the file is created
        """

        try:
            # get the value in the database
            tuples = self.data.get_tuples(
                """SELECT DateCreation 
                FROM workorders 
                WHERE NAME = ?""",
                [self.test_name]
            )
            
            # dates in string
            date_result = tuples[0][0]

            try:
                date1 = datetime.strptime(date_result, CONSTANT_FORMAT_DATES_DATABASE)
            except Exception:
                date1 = datetime.strptime(date_result, CONSTANT_SHORT_FORMAT_DATES_DATABASE)

            date2 = datetime.strptime(folder_creation_time, "%Y-%m-%d_%Hh%Mm%Ss")
    
            # calculate the difference between the two dates and define the tolerance at 2 minutes
            diff = abs(date1 - date2)
            tolerance = timedelta(minutes=1)

            if diff <= tolerance:
                content_list.append("-> Date de création du test => OK")
                content_list.append(f"   - Valeur obtenue : {date1}")
                content_list.append(f"   - Valeur expectée : {date2}")
            else:
                content_list.append("-> Date de création du test => NOK")
                content_list.append(f"   - Valeur obtenue : {date1}")
                content_list.append(f"   - Valeur expectée : {date2}")
        except Exception as e:
            content_list.append(f"==> [ERREUR] Date de création du test => {e}")

        content_list.append(" ")


    def check_start_end_date_card(self, content_list: list):
        """ `+`
        `Type:` Procedure
        `Description:` checking the consistency of the start and end dates of a card
        :param:`content_list:` file content
        """

        # verification of start date and end date
        try:
            # get the value in the database
            date_tuples = self.data.get_tuples(
                """SELECT w.DateBegin, w.DateEnd 
                FROM workorders wo 
                JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder 
                JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine 
                WHERE wo.Name = ?""",
                [self.test_name]
            )

            # get the production time of the card and the number of cards to make in the database
            max_time_tuple = self.data.get_tuples(
                """SELECT MAX(wrms.ExpectedCycleTime), (w.NbUnitsToDo div wrm.NbUnitsPerWork) AS cartes 
                FROM workorders w 
                JOIN workorderrecipemachines wrm ON w.IdWorkOrder = wrm.IdWorkOrder 
                JOIN workorderrecipemachinestages wrms ON wrm.IdWorkOrderRecipeMachine = wrms.IdWorkOrderRecipeMachine 
                WHERE w.Name = ?""", 
                [self.test_name]
            )

            # decomposition of the tuple to calculate the max production time
            unit_time = float(max_time_tuple[0][0])
            nb_cards_to_made = int(max_time_tuple[0][1])
            time_for_a_card = unit_time/1000
            time_for_cards = time_for_a_card * nb_cards_to_made

            content_list.append("-> Cohérence des dates de début et de fin d'une carte")

            for i in range(0, len(date_tuples)):
                content_list.append(f"  => Carte N°{i+1}")

                try:
                    begin_date = datetime.strptime(date_tuples[i][0], CONSTANT_FORMAT_DATES_DATABASE)
                except Exception:
                    begin_date = datetime.strptime(date_tuples[i][0], CONSTANT_SHORT_FORMAT_DATES_DATABASE)

                try:
                    end_date = datetime.strptime(date_tuples[i][1], CONSTANT_FORMAT_DATES_DATABASE)
                except Exception:
                    end_date = datetime.strptime(date_tuples[i][1], CONSTANT_SHORT_FORMAT_DATES_DATABASE)

                max_end_date = begin_date + timedelta(seconds=time_for_cards)

                # consistency test of start and end dates
                if i != 0:
                    try:
                        before_begin_date = datetime.strptime(date_tuples[i-1][0], CONSTANT_FORMAT_DATES_DATABASE)
                    except Exception:
                        before_begin_date = datetime.strptime(date_tuples[i-1][0], CONSTANT_SHORT_FORMAT_DATES_DATABASE)

                    try:
                        before_end_date = datetime.strptime(date_tuples[i][1], CONSTANT_FORMAT_DATES_DATABASE)
                    except Exception:
                        before_end_date = datetime.strptime(date_tuples[i][1], CONSTANT_SHORT_FORMAT_DATES_DATABASE)

                    # test of the start date of the card between start and end of the card before
                    if before_begin_date < begin_date and begin_date < before_end_date:
                        content_list.append("       -> Date de début de la carte comprise entre début et fin de la carte d'avant => OK")
                        content_list.append(f"          - Date de début : {begin_date}")
                        content_list.append(f"          - Date de début de la carte d'avant : {before_begin_date}")
                        content_list.append(f"          - Date de fin de la carte d'avant : {before_end_date}")
                    else:
                        content_list.append("       -> Date de début de la carte comprise entre début et fin de la carte d'avant => NOK")
                        content_list.append(f"          - Date de début : {begin_date}")
                        content_list.append(f"          - Date de début de la carte d'avant : {before_begin_date}")
                        content_list.append(f"          - Date de fin de la carte d'avant : {before_end_date}")

                # consistency test of start and end dates
                if begin_date < end_date and end_date <= max_end_date:
                    content_list.append("       -> Cohérence des date de début et de fin d'une carte => OK")
                    content_list.append(f"          - Date de début : {begin_date}")
                    content_list.append(f"          - Date de fin : {end_date}")
                    content_list.append(f"          - Date de fin maximum : {max_end_date}")
                else:
                    content_list.append("       -> Cohérence des date de début et de fin d'une carte => NOK")
                    content_list.append(f"          - Date de début : {begin_date}")
                    content_list.append(f"          - Date de fin : {end_date}")
                    content_list.append(f"          - Date de fin maximum : {max_end_date}")
        except Exception as e:
            content_list.append(f"==> [ERREUR] Cohérence des dates de début et de fin de la production d'une carte => {e}")

        content_list.append(" ")


    def check_date_begin_equal_start(self, content_list: list, start_time: str):
        """ `+`
        `Type:` Procedure
        `Description:` 
        :param:`content_list:` file content
        :param:`start_time:` time when you press start
        """

        try:
            # get the value in the database
            date_tuples = self.data.get_tuples(
                """SELECT w.DateBegin
                FROM workorders wo 
                JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder 
                JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine 
                WHERE wo.Name = ?
                LIMIT 1;""",
                [self.test_name]
            )
            
            # dates in string
            date_result = date_tuples[0][0]

            try:
                date1 = datetime.strptime(date_result, CONSTANT_FORMAT_DATES_DATABASE)
            except Exception:
                date1 = datetime.strptime(date_result, CONSTANT_SHORT_FORMAT_DATES_DATABASE)

            date2 = datetime.strptime(start_time, CONSTANT_SHORT_FORMAT_DATES_DATABASE)
    
            # calculate the difference between the two dates and define the tolerance at 2 minutes
            diff = abs(date1 - date2)
            tolerance = timedelta(minutes=1)

            if diff <= tolerance:
                content_list.append("-> Date de mise en marche du test => OK")
                content_list.append(f"   - Valeur obtenue : {date1}")
                content_list.append(f"   - Valeur expectée : {date2}")
            else:
                content_list.append("-> Date de mise en marche du test => NOK")
                content_list.append(f"   - Valeur obtenue : {date1}")
                content_list.append(f"   - Valeur expectée : {date2}")
        except Exception as e:
            content_list.append(f"==> [ERREUR] Date de mise en marche du test => {e}")

        content_list.append(" ")


    def test_begin_date_constency(self, content_list : list, folder_creation_time: str):
        """ `+`
        `Type:` Procedure
        `Description:` verification of the consistency of the begin date in workorderactivationhistory
        :param:`content_list:` file content
        :param:`folder_creation_time:` time the file is created
        """

        try:
            # get the value in the database
            date_tuples = self.data.get_tuples(
                """SELECT woah.DateBegin
                FROM workorders wo 
                JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder
                JOIN workorderactivationshistory woah ON woah.IdWorkOrderRecipeMachine = worm.IdWorkOrderRecipeMachine
                WHERE wo.Name = ?""",
                [self.test_name]
            )
            
            # dates in string
            date_result = date_tuples[0][0]

            try:
                date1 = datetime.strptime(date_result, CONSTANT_FORMAT_DATES_DATABASE)
            except Exception:
                date1 = datetime.strptime(date_result, CONSTANT_SHORT_FORMAT_DATES_DATABASE)

            date2 = datetime.strptime(folder_creation_time, "%Y-%m-%d_%Hh%Mm%Ss")
    
            # calculate the difference between the two dates and define the tolerance at 2 minutes
            diff = abs(date1 - date2)
            tolerance = timedelta(minutes=1)

            if diff <= tolerance:
                content_list.append("-> Date de validation du test => OK")
                content_list.append(f"   - Valeur obtenue : {date1}")
                content_list.append(f"   - Valeur expectée : {date2}")
            else:
                content_list.append("-> Date de validation du test => NOK")
                content_list.append(f"   - Valeur obtenue : {date1}")
                content_list.append(f"   - Valeur expectée : {date2}")
        except Exception as e:
            content_list.append(f"==> [ERREUR] Date de validation du test => {e}")

        content_list.append(" ")


    ################################################################ Component section ################################################################


    def nb_components_installed(self, content_list: list):
        """ `+`
        `Type:` Procedure
        `Description:` verification of the number of components installed per card
        :param:`content_list:` file content
        """

        try:
            # get the values in the database
            # number of components per card
            nb_components_tuples = self.data.get_tuples(
                """SELECT worm.NbUnitsPerWork, worm.NbComponentsPerUnit 
                FROM workorders wo 
                JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder 
                WHERE wo.Name = ?""",
                [self.test_name]
            )
            
            nb_unit_per_work = nb_components_tuples[0][0]
            nb_components_per_unit = nb_components_tuples[0][1]
            nb_components_per_card_expected = int(nb_unit_per_work) * int(nb_components_per_unit)

            # id of the cards
            id_work_tuples = self.data.get_tuples(
                """SELECT w.IdWork 
                FROM workorders wo 
                JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder 
                JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine 
                WHERE wo.Name = ?""",
                [self.test_name]
            )

            flat_list = [element for sub_list in id_work_tuples for element in sub_list]

            content_list.append("-> Nombre de composants posés par carte")

            # for each card we check the number of components placed
            for i, id_work in enumerate(flat_list):

                content_list.append(f"  => Carte N°{i+1}")

                # number of components installed for this card
                nb_components_installed_tuples = self.data.get_tuples(
                    """SELECT COUNT(*) 
                    FROM workorders wo 
                    JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder 
                    JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine 
                    JOIN activities a ON w.IdWork = a.IdWork 
                    JOIN components c ON c.IdActivity = a.IdActivity 
                    WHERE wo.Name = ? AND w.IdWork = ?""",
                    [self.test_name, id_work]
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