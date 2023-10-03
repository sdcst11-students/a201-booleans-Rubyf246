#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

a = float(input ("Give me a number, then press enter."))
b=a%1
if b == 0:
  print("the number is an integer")
if b!=0:
  print("the number is not an integer ")