# Author        : Victor BROSSARD
# Description   : Object that opens simulator and RC

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
from PathsInit.PathsInit import _PathsInit

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
        
        # Open software
        self._start_simu()
        self._start_rc()