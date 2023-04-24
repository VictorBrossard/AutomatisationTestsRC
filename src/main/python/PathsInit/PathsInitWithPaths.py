# Author        : Victor BROSSARD
# Description   : Object that opens simulator and RC

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
from PathsInit.PathsInit import _PathsInit
from UsefulFunction.UsefulFunction import is_soft_open

#-----------------------------------------------------------------------------------------------------   

class PathsInitWithPaths(_PathsInit):
    """ `+`
    :class:`PathsInitWithoutPaths` is a child class of PathsInit which knows the paths of the software 
    """

    def __init__(self, simu_way: str, rc_way: str):
        """ `-`
        `Type:` Constructor
        """

        # Parent constuctor
        _PathsInit.__init__(self)

        # Initializes object variables
        self.simu_path = simu_way
        self.rc_path = rc_way
        
        # Open software if closed
        if not is_soft_open("Simulat.exe"):
            self._start_simu()
            
        if not is_soft_open("rc5.exe"):
            self._start_rc()