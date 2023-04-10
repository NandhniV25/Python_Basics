"""
The first line should contain the value of r.
The second line should contain the value of o.
A polar coordinate (r,o)

is completely determined by modulus r and phase angle o.

If we convert complex number z  to its polar coordinate, we find:
r: Distance from z  to origin, i.e., square root of x^2+y^2
o: Counter clockwise angle measured from the positive x-axis to the line segment that joins  to the origin.

Python's cmath module provides access to the mathematical functions for complex numbers.
"""
import cmath
z=complex(input())
print(abs(z))#r
print(cmath.phase(z))