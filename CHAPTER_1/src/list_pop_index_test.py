from timeit import Timer
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from pylab import *

start = 1001
ceiling = 1000000
step = 1000
t1_data = {
    'x' : [ ] ,
    'y' : [ ]
}

test_case = Timer( "n.pop(0)" , "from __main__ import n" )
for i in range( start, ceiling, step ):
    n = list( range( i ) )
    t1 = test_case.timeit(number=1000)
    t1_data[ 'y' ].append( t1 )
    t1_data[ 'x' ].append( i )

fig = plt.figure()
plt.plot( 
    t1_data[ 'x' ], t1_data[ 'y' ], color='r', linestyle='-', linewidth=2, label="list.pop(index)" 
)
plt.ylabel( "Milliseconds to complete" )
plt.xlabel( "Size of List ( K )" )

#
#  plot linear constant to compare
#
fit = polyfit( t1_data[ 'x' ], t1_data[ 'y' ], 1 )
fit_fn = poly1d( fit ) # fit_fn is now a function which takes in x and returns an estimate for y
c1 = np.arange( start, ceiling, step ) # evenly sampled time at 200ms intervals
plt.plot( 
    t1_data[ 'x' ], fit_fn( t1_data[ 'x' ] ), color='g', linestyle='-', linewidth=2, label="fit" 
)
plt.plot( 
    [ start, ceiling ], [ min( t1_data[ 'y' ] ), max( t1_data[ 'y' ] ) ], color='k', linestyle='--', linewidth=2, label="linear" 
)
fig.suptitle( 'List .pop(index)', fontsize=13 )
legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


        
