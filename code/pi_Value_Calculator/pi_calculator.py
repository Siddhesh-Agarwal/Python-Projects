################################################################################
##  INFORMATION                                                               ##
##  Newtons method of calculating pi                                          ##
##  P(n + 1) = P(n) + sin(P(n)), n>=0                                         ##
##  P(0) = 3                                                                  ##
##  accuracy of program increases with each iteration( i.e from loop=3 )      ##
##  READ MORE: http://mathforum.org/library/drmath/view/65244.html            ##
################################################################################

loop = int(input("number of times loop needs to be executed: "))
def pi_value(n):
    pi = 3
    for a in range(n):
        pi += m.sin(pi)
        if m.sin(pi) == 0:
            break
    return pi

print("pi value (by calculations): ", pi_value(loop) )

import math as m
print("pi value (by math module):  ", m.pi)
