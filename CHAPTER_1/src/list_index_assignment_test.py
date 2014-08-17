from timeit import Timer
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from pylab import *

start = 1
ceiling = 50000
step = 100

label = "n[idx]"
test_case = Timer("n[idx]=None", "from __main__ import n, idx")
t1_data = { 'x' : [], 'y' : [] } 
for i in range( start, ceiling, step ):
    n = list( range( i ) )
    idx = len( n ) / 2
    t1 = test_case.timeit( number=1000 )
    t1_data[ 'y' ].append( t1 )
    t1_data[ 'x' ].append( i )

fig = plt.figure()
plt.plot( 
    t1_data[ 'x' ], t1_data[ 'y' ], 'r',  label=label
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
plt.plot( 
    [ start, ceiling ], [ min( t1_data[ 'y' ] ), max( t1_data[ 'y' ] ) ], color='k', linestyle='--', linewidth=1, label="linear" 
)
fig.suptitle( 'List '+label, fontsize=13 )
legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
        
