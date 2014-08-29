#
#  https://projecteuler.net/problem=1
#
#
#  Q: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#  The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
#
#  A: 532n + 1000
# 
#  A: O( log n )
#
#

nsum = 0
end = 7000
for i in range( 1, end ):
    if i % 3 == 0 or i % 5 == 0:
        print i
        nsum += i

print "[ NSUM ]: %s" % nsum 
factors_of_3 = end / 3
factors_of_5 = end / 5
print "[ TOTAL FACTOR(s) ]: %s" % ( factors_of_3 + factors_of_5 )
