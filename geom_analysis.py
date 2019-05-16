"""
Functions and scripts for geometry analysis
"""

#This is my geometry analysis code
import numpy
import os
import sys  #Is going to allow for user input, gets variables from command line

def calculate_distance(atom1, atom2):
    """
    Calculate the distance between two atoms.

    Parameters
    ----------
    atom1: list
        A list of coordinates [x, y, z]
    atom2: list
        A list of coordinates [x, y, z]

    Returns
    -------
    distance: float
        The distance between atoms.

    Examples
    --------
    >>> calculate_distance([0, 0, 0], [0, 0, 1])
    1.0

    """
    x_distance = atom1[0]-atom2[0]
    y_distance = atom1[1]-atom2[1]
    z_distance = atom1[2]-atom2[2]
    distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance

def bond_check(bond_distance, minimum = 0.0, maximum = 1.5):#min and max are set to default values if user
    """
    Check if the bond distance is within specified parameters before printing.

    Parameters
    ----------
    bond_distance: float
        The bond length calculated in calculate_distance.

    minimum: float
        Minimum accepted distance for a reported bond, default is 0.0
    maximum: float
        Maximum accepted distance for a reported bond, default is 1.5

    Returns
    -------
    True: boolean
        True if the bond is within the acceptable range
    False: boolean
        False if the bond is not within the acceptable range
    """
    #Check that atom distance is a float
    if not isinstance(bond_distance, float):
        raise TypeError(F'bond_distance must be type float. {bond_distance}')

    if bond_distance < maximum and bond_distance > minimum:  #forgets to set min or max
        return True
    else:
        return False

if __name__ == "__main__":  #Tells python that if this is run as a script execute everything underneath.
    if len(sys.argv) < 2:
        raise IndexError('No file name given. Script require xyz file')

    file_location = sys.argv[1] #File location specified by user; sys.argv[0] is our program so argv[1] allows for input after running the program
    xyz_file = numpy.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')

    symbols = xyz_file[:,0]
    coordinates = xyz_file[:,1:]
    coordinates = coordinates.astype(numpy.float)

    for numA, atomA in enumerate(coordinates):
        for numB, atomB in enumerate(coordinates):
            if numB < numA:
                distance_AB = calculate_distance(atomA, atomB)
                if bond_check(distance_AB) == True:
                    print(F'{symbols[numA]} to {symbols[numB]}: {distance_AB: .3f}')
