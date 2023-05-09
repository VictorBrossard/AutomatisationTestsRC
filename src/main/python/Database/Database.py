# Author        : Victor BROSSARD
# Description   : Class that manages the interaction with the database

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import mariadb
import sys
import os

from FilesManagement.Files.ManageFiles import ManageFiles
from FilesManagement.Files.ManageFiles import CONSTANT_NAME_DATABASE_FILE
from FilesManagement.Folders.ManageFolders import CONSTANT_SETTINGS_FOLDER_PATH

from GraphicInterface.MessageBox import MessageBox
from GraphicInterface.SimpleQuestionInterface import SimpleQuestionInterface

#-----------------------------------------------------------------------------------------------------

class Database(object):
    """ `+`
    :class:`Database` manages the interaction with the database
    """
    
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        self.manage_file = ManageFiles()
        self.manage_file.create_database_settings_file()

        settings_database = self.manage_file.get_database_lines()

        self.name_database = settings_database[4]
        self.cursor = self.__connect(
            settings_database[0],       # Username
            settings_database[1],       # Password
            settings_database[2],       # Host
            int(settings_database[3]),  # Port
            self.name_database          # Database
        )


    def __connect(self, user: str, password: str, host: str, port: int, database: str):
        """ `+`
        `Type:` Procedure
        `Description:` Connect our program to mariadb
        :param:`user:` user ID of the database
        :param:`password:` user password of the database
        :param:`host:` host ip
        :param:`port:` port of the database
        :param:`database:` name of the database
        `Return:` cursor to manipulate the database
        """

        # Connect to MariaDB Platform
        try:
            self.connector = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database
            )
        except mariadb.Error as e:
            MessageBox("ERREUR Connection", f"[ERREUR] Connection à la base de donnée : {e}").mainloop()
            question = SimpleQuestionInterface("Reconnection", "Voulez-vous essayer de vous reconnecter ?")
            question.mainloop()

            if question.get_is_yes():
                os.remove(f"{CONSTANT_SETTINGS_FOLDER_PATH}\\{CONSTANT_NAME_DATABASE_FILE}")
                self.__init__()
                return
            else:
                os.remove(f"{CONSTANT_SETTINGS_FOLDER_PATH}\\{CONSTANT_NAME_DATABASE_FILE}")
                sys.exit(1)

        return self.connector.cursor()
    

    def close_connection(self):
        """ `+`
        `Type:` Procedure
        `Description:` close the connection with the database
        """

        self.connector.close()


    def deletes_all_tuples(self):
        """ `+`
        `Type:` Procedure
        `Description:` deletes all data from the database
        """

        # retrieve the name of all the tables in the database
        self.cursor.execute(
            "SHOW TABLES FROM ?",
            (self.name_database,)
        )

        # deactivation of constraints
        self.cursor.execute(
            "SET FOREIGN_KEY_CHECKS = 0;",
            ()
        )

        rows = self.cursor.fetchall()

        # deletion of tuples from each table
        for table_name in rows:
            self.cursor.execute(
                "DELETE FROM ?",
                (table_name,)
            )

        # activation of constraints
        self.cursor.execute(
            "SET FOREIGN_KEY_CHECKS = 1;",
            ()
        )


    def save_all_tuples(self, path: str):
        """ `+` 
        `Type:` Procedure
        `Description:` saves all tuples of all tables in the database
        :param:`path:` path to save the file
        """

        # retrieve the name of all the tables in the database
        self.cursor.execute(
            "SHOW TABLES FROM ?",
            (self.name_database,)
        )

        rows = self.cursor.fetchall()

        for row in rows:
            self.__save_table_tuples(row, path)


    def __save_table_tuples(self, table_name: str, path: str):
        """ `-`
        `Type:` Procedure
        `Description:` saves in a file all the tuples of a table
        :param:`table_name:` name of the table of tuples to retrieve
        :param:`path:` path to save the file
        """

        # selection of the tuples of the table
        self.cursor.execute(
            "SELECT * FROM ?",
            (table_name)
        )

        rows = self.cursor.fetchall()

        self.manage_file.create_file(path, f"{table_name}.txt", rows)


    def get_tuples(self, command: str, variable_list: list) -> list:
        """ `+`
        `Type:` Function
        `Description:` gets all tuples of the command given in parameter
        :param:`command:` command to be executed
        :param:`varaible_list:` list of variables in the command
        `Return:`
        """

        self.cursor.execute(
            command,
            (','.join(variable_list),)
        )

        return self.cursor.fetchall()

    
    def get_nb_cards(self, test_name: str) -> int:
        """
        """

        self.cursor.execute(
            "SELECT IdWorkOrder, NbUnitsToDo FROM promon.workorders WHERE workorders.Name = ?",
            (test_name,)
        )

        rows = self.cursor.fetchall()

        if len(rows) != 1:
            return 0
        else:
            return rows


    def get_time_prod_card(self, test_name: str) -> int:
        """
        """

        self.cursor.execute(
            "SET FOREIGN_KEY_CHECKS = 1;",
            (test_name,)
        )

        rows = self.cursor.fetchall()

        if len(rows) != 1:
            return 0
        else:
            return rows