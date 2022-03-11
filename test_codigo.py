""" 
Muestra como testear una funcion con el modulo doctest.
ejecutar: python test_codigo.py -v para correr el test
"""

import re

def dni_valid(dni):
    """
    >>> dni_valid('12345678')
    True

    >>> dni_valid('123456789')
    False

    >>> dni_valid('12345678A')
    False
    """

    if re.match('[0-9]{8}$', dni):
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()        