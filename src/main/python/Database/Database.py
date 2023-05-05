# Author        : Victor BROSSARD
# Description   : Class that manages the interaction with the database

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import mariadb
import sys

from FilesManagement.Files.ManageFiles import ManageFiles

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

        self.__connect("europlacer", "", "127.0.0.1", 3306, "promon")


    def __connect(self, user: str, password: str, host: str, port: int, database: str):
        """ `+`
        `Type:` Procedure
        `Description:` Connect our program to mariadb
        :param:`user:` user ID of the database
        :param:`password:` user password of the database
        :param:`host:` host ip
        :param:`port:` port of the database
        :param:`database:` name of the database
        """

        # Connect to MariaDB Platform
        try:
            connector = mariadb.connect(
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
                self.__connect(user, password, host, port, database)
            else:
                sys.exit(1)