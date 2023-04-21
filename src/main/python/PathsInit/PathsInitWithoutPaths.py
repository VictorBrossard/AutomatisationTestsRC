# Author        : Victor BROSSARD
# Description   : Object that opens simulator and RC

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
from PathsInit.PathsInit import _PathsInit

#-----------------------------------------------------------------------------------------------------

class PathsInitWithoutPaths(_PathsInit):
    """ `+`
    :class:`PathsInitWithoutPaths` is a child class of PathsInit which doesn't know the paths of the software 
            so we will ask the user for them
    """

    # Constructor
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        # Parent constuctor
        _PathsInit.__init__(self)

        # Initializes object variables
        self.simu_path = self._simu_init()
        self.rc_path = self._rc_init()
        
        # Open software
        self._start_simu()
        self._start_rc()