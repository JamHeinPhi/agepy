from scipy import constants


h = constants.h
c = constants.c
e = constants.e

def wavelength2ev(wavelength):
    """
    Function to convert a wavelength in m and converts it into an energy in eV
    
    wavelength: wavenlength in m to be converted
    returns: the energy value in eV
    """
    return h * c / (e*wavelength)


def ev2wavelength(energy):
    """
    Function to convert a energy in eV and converts it into a wavelength in m
    
    energy: energy in eV to be converted
    returns: the wavelength value in m
    """
    return 1 / (energy * e / (h * c))