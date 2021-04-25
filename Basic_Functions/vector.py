"""
vector.py

This program defines a vector and the 
basic operations associated with it.

Author: Adarsh

"""

import math


class Vector:
    """
    This program creates a vector and also
    enables the operations of vector algebra on 
    it.

    """

    def __init__(self, comp):
        """
        Initializes the vector in two possible 
        ways. If given a list, it creates a vector
        with the components of the list. If given an
        integer n, it creates the n-dimensional zero
        vector.

        >>> v = Vector([1, 2, 3])
        >>> v.components
        [1, 2, 3]
        >>> v.dim
        3

        >>> r = Vector(2)
        >>> r.components
        [0, 0]

        >>> r.dim
        2
        """
        if isinstance(comp, list):
            self.components = comp
            self.dim = len(comp)
        elif isinstance(comp, int):
            self.dim = comp
            self.components = [0 for i in range(comp)]

    def __neg__(self):
        """
        This negates a vector by negating each
        of its components.

        >>> v = Vector([1, -2, 34])
        >>> v = -v
        >>> print(v)
        <BLANKLINE>
        Dimension of vector: 3
        The vector:
         -1
          2
        -34
        <BLANKLINE>

        """
        result = []
        for c in self.components:
            result.append(-c)
        vr = Vector(result)
        return vr

    def __eq__(self, other):
        """
        Checks if two vectors are equal by comparing
        components.

        >>> v1 = Vector([1, 2, 3])
        >>> v2 = eval(repr(v1))
        >>> v1 == v2
        True

        >>> v3 = Vector([1, 2])
        >>> v3 == v1
        False

        >>> v3 = Vector([1, 2, -3])
        >>> v3 == v1
        False
        """
        equal = False
        if (self.dim == other.dim):
            equal = True

        if equal:
            for i in range(self.dim):
                if self.components[i] != other.components[i]:
                    equal = False
                    break

        if equal:
            return True
        else:
            return False

    def __add__(self, other):
        """
        This adds two vectors according to the 
        laws of vector addition if the addition 
        is compatible

        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([-1, 5, 6])
        >>> v = v1 + v2
        >>> print(v)
        <BLANKLINE>
        Dimension of vector: 3
        The vector:
         0
         7
         9
        <BLANKLINE>

        """
        if self.dim != other.dim:
            Vector.__comp_mismatch(self, other)
            return

        result = []
        for i in range(self.dim):
            result.append(self.components[i] + other.components[i])
        vr = Vector(result)
        return vr

    def __iadd__(self, other):
        """
        Shorthand addition.

        >>> v1 = Vector([1, 2, 3])
        >>> v1 += v1
        >>> v1
        Vector([2, 4, 6])
        """
        return self + other

    def __sub__(self, other):
        """
        Subtracts two vectors according
        to the laws of vector subtraction. Note that
        the second vector is subtracted from the 
        first and not the other way. Works only if
        the vectors have compatible dimensions.

        >>> v1 = Vector([1, 2])
        >>> v2 = Vector([-10, 0])

        >>> print(v1 - v2)
        <BLANKLINE>
        Dimension of vector: 2
        The vector:
         11
         2
        <BLANKLINE>

        >>> v3 = Vector([1, 2, 3])
        >>> print(v1 - v3)
        Traceback (most recent call last):
        ...
        ValueError: The operation is not supported. 2 with 3
        """
        return self + (-other)

    def __isub__(self, other):
        """
        Shorthand subtraction.

        >>> v = Vector([1, 2, 3])
        >>> v -= v
        >>> v
        Vector([0, 0, 0])
        """
        return self - other

    def dot(self, other):
        """
        Returns the standard inner product of the
        two vectors in terms of their components, 
        provided that they have identical dimensions.
        Else raises an exception.

        >>> v1 = Vector([10, 9, 3])
        >>> v2 = Vector([-1, 4, 2])
        >>> v1.dot(v2)
        32

        >>> v3 = Vector(2)
        >>> v1.dot(v3)
        Traceback (most recent call last):
        ...
        ValueError: The operation is not supported. 3 with 2
        """
        if (self.dim != other.dim):
            Vector.__comp_mismatch(self, other)
            return

        result = 0
        for i in range(self.dim):
            result += self.components[i] * other.components[i]
        return result

    def __str__(self):
        """
        This returns the representation of the vector 
        in a form that can be understood by the user.

        >>> v = Vector([1, 2, 3])

        >>> print(v)
        <BLANKLINE>
        Dimension of vector: 3
        The vector:
         1
         2
         3
        <BLANKLINE>

        >>> v3 = Vector(2)
        >>> print(v3)
        <BLANKLINE>
        Dimension of vector: 2
        The vector:
         0
         0
        <BLANKLINE>

        """
        largest = 0
        for c in self.components:
            if abs(c) > largest:
                largest = c
        length = len(str(largest))

        result = ""
        result += "\nDimension of vector: {0}\n" \
            .format(self.dim)
        result += "The vector:\n"

        for c in self.components:
            result += ("{0:> " + str(length) + "}\n").format(c)
        return result

    def __repr__(self):
        """
        Returns an eval-avble expression of given Vector.

        >>> v = Vector([1, 2, 3])
        >>> print(repr(v))
        Vector([1, 2, 3])

        >>> v1 = eval(repr(v))
        >>> print(v1)
        <BLANKLINE>
        Dimension of vector: 3
        The vector:
         1
         2
         3
        <BLANKLINE>
        """
        return ("Vector(" + str(self.components) + ")")

    def __comp_mismatch(self, other):
        raise ValueError("The operation is not supported. {0} with {1}"
                         .format(self.dim, other.dim))

    @property
    def length(self):
        """
        Returns the length of the vector with
        respect to the standard inner product.

        >>> v = Vector([3, 4])
        >>> v.length
        5.0

        >>> v = Vector([3, 4, math.sqrt(11)])
        >>> v.length
        6.0
        """
        return math.sqrt(self.dot(self))

    @staticmethod
    def angle(self, other):
        """
        Returns the angle between two vectors of the 
        same dimension in radians.

        >>> v1 = Vector([3, 5])
        >>> v2 = Vector([-5, 3])
        >>> Vector.angle(v1, v2)
        1.5707963267948966

        >>> Vector.angle(v1, v1)
        0.0
        """
        return math.acos(self.dot(other) / (self.length * other.length))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
