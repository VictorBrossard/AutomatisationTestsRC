# Author        : Victor BROSSARD
# Description   : Object that opens simulator and RC

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
from PathsInit.PathsInit import _PathsInit

#-----------------------------------------------------------------------------------------------------   
# Child class of Init which knows the paths of the software
class PathsInitWithPaths(_PathsInit):

    # Constructor
    def __init__(self, simu_way, rc_way):
        # Parent constuctor
        _PathsInit.__init__(self)

        # Initializes object variables
        self.simu_path = simu_way
        self.rc_path = rc_way
        
        # Open software
        self._start_simu()
        self._start_rc()