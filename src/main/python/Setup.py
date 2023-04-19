# Author        : Victor BROSSARD
# Description   : 

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import ctypes
import sys

#-----------------------------------------------------------------------------------------------------
#
def run_as_admin():
    """
    Demande une autorisation d'administrateur et redémarre le script.
    """
    if ctypes.windll.shell32.IsUserAnAdmin():
        return
    else:
        # Redémarre le script avec des droits d'administrateur
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)