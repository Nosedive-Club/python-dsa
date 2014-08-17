from timeit import Timer
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

start = 1001
ceiling = 50000
step = 100
t1_data = {
    'x' : [ ] ,
    'y' : [ ]
}

test_case = Timer( "n.insert( idx, 999 )" , "from __main__ import n, idx" )
for i in range( start, ceiling, step ):
    n = list( range( i ) )
    idx = len( n ) / 2
    t1 = test_case.timeit(number=1000)
    t1_data[ 'y' ].append( t1 )
    t1_data[ 'x' ].append( i )

fig = plt.figure()
plt.plot( 
    t1_data[ 'x' ], t1_data[ 'y' ], color='r', linestyle='-', linewidth=2, label="list.insert(index,n)" 
)
plt.ylabel( "Milliseconds to complete" )
plt.xlabel( "Size of List ( K )" )
#
#  plot constants as lines to compare output
#
c1 = np.arange( start, ceiling, step ) # evenly sampled time at 200ms intervals
c2 = [1]*( ceiling / step )
plt.plot( 
    c1, c1, color='k', linestyle='-', linewidth=2, label="linear" 
)
plt.plot(
    c2, c2, color='k', linestyle='-', linewidth=2, label="constant" 
)

fig.suptitle( 'List .insert(index,n)', fontsize=13 )
legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


        
