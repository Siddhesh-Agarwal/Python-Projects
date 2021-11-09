################################################################################
##  INFORMATION                                                               ##
##  Newtons method of calculating pi                                          ##
##  P(n + 1) = P(n) + sin(P(n)), n>=0                                         ##
##  P(0) = 3                                                                  ##
##  accuracy of program increases with each iteration( i.e from loop=3 )      ##
##  READ MORE: http://mathforum.org/library/drmath/view/65244.html            ##
################################################################################
from math import sin

def pi(n):
    pi = 3                   # No, I am not joking
    for a in range(n):
        pi += sin(pi)
        if sin(pi) == 0:     # Value wouldn't increase since, sin(pi) = 0
            break
    return pi

loop = int(input("number of times loop needs to be executed: "))
print("pi value (by calculations): ", pi(loop) )

from math import pi          # Displaying actual value of pi 
print("pi value (by math module):  ", pi)
