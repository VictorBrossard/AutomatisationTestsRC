# Author        : Victor BROSSARD
# Description   : Object that opens simulator and RC

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
from PathsInit.PathsInit import PathsInit

#-----------------------------------------------------------------------------------------------------
# Child class of Init which does not know the paths of the software so we will ask the user for them
class PathsInitWithoutPaths(PathsInit):

    # Constructor
    def __init__(self):
        # Parent constuctor
        PathsInit.__init__(self)

        # Initializes object variables
        self.simu_path = self.simu_init()
        self.rc_path = self.rc_init()
        
        # Open software
        self.start_simu()
        self.start_rc()