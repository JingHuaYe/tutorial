def to_the_power(x, y):
 y = 2
 result = x
 for i in range(0, y):
  result *= x
 return result

def main():
 x = 10
 y = 3
 print "10 to the power of 3 is: ", to_the_power(x, y)

main()
