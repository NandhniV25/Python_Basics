
import math
a = int(input())
b = int(input())

# finding distace and angle
M = math.sqrt(a**2+b**2)
theta = math.acos(b/M )

# printing the angle
print(int(round(math.degrees(theta),0)),'\u00B0',sep='')