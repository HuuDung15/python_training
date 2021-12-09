"""
Calculator
==========

Build support functions for Linear Algebra operations
"""


# =============================================================================


__author__ = 'Nguyễn Hữu Dũng'
__email__ = 'nhuudung10@gmail.com'
__date__ = '2021/12/05'
__status__ = 'development'


# =============================================================================


import math


class Vector(object):
    """ Create a vector """
    def __init__(self, *args):
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args
    
    def norm(self):
        return math.sqrt(sum(x*x for x in self))


# =============================================================================


    def inner(self, vector):
        if not isinstance(vector, Vector):
            raise ValueError('The dot product requires another vector')
        return sum(a*b for a, b in zip(self, vector))
        


# =============================================================================


    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.inner(other)
        elif isinstance(other, (int, float)):
            product = tuple(a * other for a in self)
            return self.__class__(*product)
        else:
            raise ValueError("Multiplication with type {} not supported".format(type(other)))


# =============================================================================


    def __rmul__(self, other):
        return self.__mul__(other)


# =============================================================================


    def __truediv__(self, other):
        if isinstance(other, Vector):
            divided = tuple(a / b for a, b in zip(self, other))
        elif isinstance(other, (int, float)):
            divided = tuple(a / other for a in self)
        else: 
            raise ValueError("Division with type {} not supported".format(type(other)))

        return self.__class__(*divided)


# =============================================================================


    def __add__(self, other):
        if isinstance(other, Vector):
            added = tuple(a + b for a, b in zip(self, other))
        elif isinstance(other, (int, float)):
            added = tuple(a + other for a in self)
        else: 
            raise ValueError("Addition with type {} not supported".format(type(other)))

        return self.__class__(*added)

        
# =============================================================================


    def __radd__(self, other):
        return self.__add__(other)

        
# =============================================================================


    def __sub__(self, other):
        if isinstance(other, Vector):
            subbed = tuple(a - b for a, b in zip(self, other))
        elif isinstance(other, (int, float)):
            subbed = tuple(a - other for a in self)
        else: 
            raise ValueError("Addition with type {} not supported".format(type(other)))       
        
        return self.__class__(*subbed)

    
# =============================================================================


    def __rsub__(self, other):
        """ Called if 5 - self for instance """
        return self.__sub__(other)
        
    
# =============================================================================



    def __dist__(self, other):
        if isinstance(other, Vector):
            return math.sqrt(sum((b - a)**2 for a, b in zip(self, other)))
        else:
            raise ValueError("Magnitude with type {} not supported".format(type(other)))
        
    
# =============================================================================


    def __iter__(self):
        return self.values.__iter__()
                
    
# =============================================================================


    def __len__(self):
        return len(self.values)
                
    
# =============================================================================

    
    def __getitem__(self, key):
        return self.values[key]

                
# =============================================================================

        
    def __repr__(self):
        return str(self.values)
    
    
# =============================================================================

   
    def __eq__(self, other):
        if(self[i] == other[i] for i in range(len(self))):
            return True
        else:
            return False