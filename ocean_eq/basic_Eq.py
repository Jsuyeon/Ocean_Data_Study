import numpy as np
#fucntion to get coriolis
def coriolis(lat):
    """
    input : lat 
    unit : degree
    """
    omega=7.292115e-5 # unit : second // omega=radians per seconde
    cori=2*omega*np.sin(np.radians(lat))
    return cori

