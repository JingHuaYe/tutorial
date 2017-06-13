"""
 This is a script that calculates one number to the power of another
"""
import math
import sys

def to_the_power(x, y):
 """ 
 y = 2
 result = x
 for i in range(0, y):
  result *= x
 return result
 """
 return x ** y

def square_root(x):
 return math.sqrt(x)

def main():
 x = int(sys.argv[1])
 y = int(sys.argv[2])
 print "{0} to the power of {1} is: {2}".format(x, y, to_the_power(x, y))
 print "The square root of {0} is {1}".format(x, square_root(x))
 print "The End"

main()
