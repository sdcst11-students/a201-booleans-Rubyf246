#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""

a = int(input ("Give me a number, then press enter."))
if a > 0:
  print("the number is positive")
if a < 0:
  print("the number is negative")
if a == 0:
  print("the number is zero")