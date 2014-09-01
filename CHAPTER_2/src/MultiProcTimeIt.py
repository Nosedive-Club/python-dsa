#
#  python
#
import uuid
import time
import multiprocessing
from timeit import Timer, timeit


#
#  matplotlib
#
import matplotlib.pyplot as plt 
from matplotlib.pyplot import *
from pylab import *

#
#  app level
#
from logger import logger


class Worker( multiprocessing.Process ):
    
    def __init__( self, task_queue, result_queue, **kwargs ):
        super( Worker, self ).__init__()

        self.name = kwargs.get( 'name', str( uuid.uuid4() ) )
        self.number = kwargs.get( 'number', 1000 )
        self.storage =  { 'x' : [ ], 'y' : [] }
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task, n_arg = self.task_queue.get()
            if next_task is None:
                logger.debug( '[ EXIT ]: %s' % proc_name )
                self.task_queue.task_done()
                break

            logger.debug( '%s -- handling --> %s' % (proc_name, len( n_arg )) )

            #
            #  run it over the passed 'number' of iterations
            #
            try:
                tsums = [] 
                for i in range( self.number ):
                    t0 = time.clock()
                    next_task( n_arg )
                    t1 = time.clock() - t0
                    tsums.append( t1 )
                self.storage[ 'y' ] = sum( tsums ) / float( self.number or 1 )
                self.storage[ 'x' ] = len( n_arg )
                self.task_queue.task_done()
                self.result_queue.put(self.storage)
            except Exception, e:
                self.task_queue.task_done()
                self.result_queue.put({ 'ERROR' : e })
        return


class TaskRunner( object ):
    def __init__( self, fn, start_range=0, stop_range=5000000, step=20000, graph_label='test', number_of_workers=2 ):
        self.fn = fn
        self.stop = stop_range
        self.start = start_range
        self.step = step
        self.label = graph_label
        self.tasks = multiprocessing.JoinableQueue()
        self.results = multiprocessing.Queue()
        self.num_workers = number_of_workers or ( multiprocessing.cpu_count() * 2 )

    def __str__(self):
        return '%s * %s' % (self.a, self.b)

    def __call__(self):
        logger.debug( '[ # WORKERS ]: %d' % self.num_workers )
        workers = [ Worker( self.tasks, self.results, **{ 'name' : 'worker-%i'%i } ) for i in xrange(self.num_workers) ]
        for w in workers:
            w.start()

        for i in range( self.start, self.stop, self.step ):
            n = range( i )
            logger.debug( "[ CREATE TASK @ N ]: %s" % i )
            self.tasks.put( ( self.fn, n ) )
            
        #
        #  add a poison pill for each worker
        #  so they know when to stop
        #
        for i in xrange( self.num_workers ):
            self.tasks.put( ( None, None ) )

        self.tasks.join()  # wait for tasks to finish
        self._print_results()


    def _print_results( self ):
        data = { 'x' : [ ], 'y' : [ ] }
        while not self.results.empty():
            result = self.results.get()
            if not hasattr( result, 'ERROR' ):
                data[ 'x' ].append( result.get(  'x', 0 ) )
                data[ 'y' ].append( result.get(  'y', 0 ) )
            logger.debug( "[ RESULT ]: %s" % result  )
        data[ 'x' ].sort()
        data[ 'y' ].sort()
        self._graph_results( data )

    def _graph_results( self, data ):
        fig = plt.figure()
        plt.plot( 
            data[ 'x' ], data[ 'y' ], color='r', linestyle='-', linewidth=2, label=self.label
        )
        plt.ylabel( "Sec(s) to complete" )
        plt.xlabel( "Size of List ( K )" )

        #
        #  plot linear constant
        #  and fit to compare results
        #
        fit = polyfit( data[ 'x' ], data[ 'y' ], 1 ) 
        fit_fn = poly1d( fit ) # fit_fn is now a function which takes in x and returns an estimate for y
        plt.plot( 
            data[ 'x' ], fit_fn( data[ 'x' ] ), color='k', linestyle='-', linewidth=2, label="fit" 
        )
        plt.plot( 
            [ self.start, self.stop ], [ min( data[ 'y' ] ), max( data[ 'y' ] ) ], color='k', linestyle='--', linewidth=2, label="linear" 
        )
        fig.suptitle( self.label, fontsize=13 )
        legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        plt.show()


