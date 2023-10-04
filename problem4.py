#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
s1 = float(input ("Give me one side, then press enter."))
s2 = float(input( "Give me second side, then press enter:"))
s3 = float(input( "Give me third side, then press enter:"))

list = [s1,s2,s3]
list.sort()
A = list[0]
B = list[1]
C = list[2]
from math import acos, degrees
degree = degrees(acos((A * A + B * B - C * C)/(2.0 * A * B)))
print (degree)
if degree > 90:
    print("obtuse triangle")
elif degree==90:
    print("right triangle")
else:
    print("acute triangle")