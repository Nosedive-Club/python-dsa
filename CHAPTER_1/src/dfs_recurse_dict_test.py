from timeit import Timer
import matplotlib.pyplot as plt
import json
from matplotlib.pyplot import *
from pylab import *
from dfs import traverse_recursive_dict

start = 10
ceiling = 1500
step = 100
t1_data = {
    'x' : [ ] ,
    'y' : [ ] ,
}


label="DFS recursive on dicts" 
test_case = Timer( "fn( json_dict )" , "from __main__ import fn, json_dict" )
for i in range( start, ceiling, step ):
    fn = traverse_recursive_dict
    json_dict =  { 'root' : [] , }

    # make fake nested data
    '''
    {   
        root : [
            { '1' : 1 } ,
            { '1' : 1 } ,
            { '2' : 2 } ,
            { '1' : 1 } ,
            { '2' : 2 } ,
            { '3' : 3 } ,
        ] ,
        '1' : 1 ,
        '2' : 2 ,
        '3' : 3 ,
        
    }
    '''
    for j in list( range( i ) ):
        key, value = ( str( j ), j )
        json_dict[ 'root' ].append(  { key : value } )
        json_dict[ key ] = value
    
    t1 = test_case.timeit(number=1000)
    t1_data[ 'y' ].append( t1 )
    t1_data[ 'x' ].append( i )

fig = plt.figure()
plt.plot( 
    t1_data[ 'x' ], t1_data[ 'y' ], color='r', linestyle='-', linewidth=2, label=label
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
    t1_data[ 'x' ], fit_fn( t1_data[ 'x' ] ), color='b', linestyle='--', linewidth=0.5, label="fit" 
)
plt.plot( 
    [ start, ceiling ], [ min( t1_data[ 'y' ] ), max( t1_data[ 'y' ] ) ], color='k', linestyle='--', linewidth=2, label="linear" 
)
fig.suptitle( 'List '+label, fontsize=13 )
legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


        
