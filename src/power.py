"""
 This is a script that calculates one number to the power of another
"""
def to_the_power(x, y):
 y = 2
 result = x
 for i in range(0, y):
  result *= x
 return result

def main():
 x = 9
 y = 6 #
 print "{0} to the power of {1} is: {2}".format(x, y, to_the_power(x, y))
 print "The End"

main()
