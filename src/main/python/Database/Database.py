# Author        : Victor BROSSARD
# Description   : Class that manages the interaction with the database

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import mariadb
import sys
import os
import subprocess

from FilesManagement.Files.ManageSpecificFiles import ManageSpecificFiles

from GraphicInterface.MessageBox import MessageBox
from GraphicInterface.SimpleQuestionInterface import SimpleQuestionInterface

from Useful.AllConstant import CONSTANT_NAME_DATABASE_FILE
from Useful.AllConstant import CONSTANT_SETTINGS_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------

class Database(object):
    """ `+`
    :class:`Database` manages the interaction with the database
    """
    
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        # creation of the file containing the information supplied by the user
        self.manage_file = ManageSpecificFiles()
        self.manage_file.create_database_settings_file()

        # retrieve lines from file
        settings_database = self.manage_file.get_database_lines()

        self.username = settings_database[0]
        self.password = settings_database[1]
        self.host = settings_database[2]
        self.port = int(settings_database[3])
        self.name_database = settings_database[4]

        self.cursor = self.__connect(
            self.username,      # Username
            self.password,      # Password
            self.host,          # Host
            self.port,          # Port
            self.name_database  # Database
        )


    def __connect(self, user: str, password: str, host: str, port: int, database: str):
        """ `+`
        `Type:` Procedure
        `Description:` Connect our program to the database
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
            # reconnection request in case of failure
            MessageBox("ERREUR Connection", f"[ERREUR] Connection à la base de donnée : {e}").mainloop()
            question = SimpleQuestionInterface("Reconnection", "Voulez-vous essayer de vous reconnecter ?")
            question.mainloop()

            if question.get_is_yes():
                os.remove(f"{CONSTANT_SETTINGS_FOLDER_PATH}\\{CONSTANT_NAME_DATABASE_FILE}")
                self.__init__()
                return
            else:
                os.remove(f"{CONSTANT_SETTINGS_FOLDER_PATH}\\{CONSTANT_NAME_DATABASE_FILE}")
                sys.exit()

        return self.connector.cursor()
    

    def close_connection(self):
        """ `+`
        `Type:` Procedure
        `Description:` close the connection with the database
        """

        try:
            self.connector.commit()
            self.connector.close()
        except Exception:
            return


    def deletes_all_tuples(self):
        """ `+`
        `Type:` Procedure
        `Description:` deletes all data from the database
        """

        # deactivation of constraints
        self.cursor.execute(
            "SET FOREIGN_KEY_CHECKS = 0",
            ()
        )

        # retrieve the name of all the tables in the database
        self.cursor.execute(
            f"SHOW TABLES FROM {self.name_database}",
            ()
        )

        rows = self.cursor.fetchall()

        # deletion of tuples from each table
        for row in rows:
            str_row = str(",".join([str(x) for x in row]))
            self.cursor.execute(
                f"DELETE FROM {str_row}",
                ()
            )

        self.connector.commit()

        # activation of constraints
        self.cursor.execute(
            "SET FOREIGN_KEY_CHECKS = 1",
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
            "SHOW TABLES",
            ()
        )

        rows = self.cursor.fetchall()

        for row in rows:
            str_row = str(",".join([str(x) for x in row]))

            # command to get the data from the tables and put them in a SQL file
            subprocess.run(
                [
                    "C:\\EUROPLACER\\MariaDB\\bin\\mariadb-dump.exe", 
                    "--databases", 
                    f"{self.name_database}", 
                    "--tables", 
                    f"{str_row}",
                    "--insert-ignore",
                    "--single-transaction", 
                    "--quick",
                    "--no-create-info",
                    "--skip-add-drop-table", 
                    f"--user={self.username}", 
                    f"--password={self.password}", 
                    ">", 
                    f"{path}\\{str_row}-data.sql"
                ], 
                shell=True
            )
            
            # command to retrieve the structure of tables in a SQL file
            subprocess.run(
                [
                    "C:\\EUROPLACER\\MariaDB\\bin\\mariadb-dump.exe",
                    "--databases",
                    f"{self.name_database}", 
                    "--tables", 
                    f"{str_row}",
                    "--insert-ignore", 
                    "--single-transaction",
                    "--quick", 
                    "--no-data", 
                    "--skip-add-drop-table",
                    f"--user={self.username}", 
                    f"--password={self.password}",
                    ">", 
                    f"{path}\\{str_row}-create.sql"
                ],
                shell=True
            )

        self.connector.commit()


    def get_tuples(self, command: str, variable_list: list) -> list:
        """ `+`
        `Type:` Function
        `Description:` gets all tuples of the command given in parameter
        :param:`command:` command to be executed
        :param:`varaible_list:` list of variables in the command
        `Return:` all data retrieved by the SQL command
        """

        # SQL command execution
        self.cursor.execute(
            command,
            tuple(variable_list)
        )

        rows = self.cursor.fetchall()
        str_rows_list = []

        # List all data
        for row in rows:
            str_row = ",".join([str(x) for x in row])
            mini_list = str_row.split(',')
            str_rows_list.append(mini_list)

        self.connector.commit()

        return str_rows_list
    

    def test_execution(self, command: str, variable_list: list):
        """ `+`
        `Type:` Procedure
        `Description:` execute the command to test
        :param:`command:` command to be executed
        :param:`varaible_list:` list of variables in the command
        """

        # SQL command execution
        self.cursor.execute(
            command,
            tuple(variable_list)
        )

        rows = self.cursor.fetchall()
        str_rows_list = []

        # List all data
        for row in rows:
            str_row = ",".join([str(x) for x in row])
            mini_list = str_row.split(',')
            str_rows_list.append(mini_list)

        print(str_rows_list)

        self.connector.commit()