# Author        : Victor BROSSARD
# Description   : Object that opens simulator and RC

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
from PathsInit.PathsInit import _PathsInit

#-----------------------------------------------------------------------------------------------------
# Child class of Init which does not know the paths of the software so we will ask the user for them
class PathsInitWithoutPaths(_PathsInit):

    # Constructor
    def __init__(self):
        # Parent constuctor
        _PathsInit.__init__(self)

        # Initializes object variables
        self.simu_path = self._simu_init()
        self.rc_path = self._rc_init()
        
        # Open software
        self._start_simu()
        self._start_rc()