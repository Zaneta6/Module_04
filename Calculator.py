# Calculation() function provides a simple tool for basic calculation.
# Operator allows to choose a requested operation - additing, subtracting, multiplying and dividing - based on selected index (1-4).
# The "a" and "b" parameters indicate the subjects of the operation (integers).

import sys

import logging
logging.basicConfig(level=logging.DEBUG)

def calculation(operator, a, b):
  result = 0
  if operator == 1:
    result = result + (a + b)
  elif operator == 2:
    result = result + (a - b)
  elif operator == 3:
    result = result + (a * b)
  elif operator == 4:
    result = result + (a/b)
  else:
    print("Error. Incorrect operator index.")
    exit(1)
  return result

if __name__ == "__main__":
  operator = int(input("Select operation type: (1 - addition, 2 - subtraction, 3 - multiplication, 4 - division) "))
  a = int(input("Select the first number: "))
  b = int(input("Select the second number: "))
  calculation_result = calculation(operator, a, b)
  print(calculation_result)