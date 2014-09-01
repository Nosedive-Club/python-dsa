from MultiProcTimeIt import TaskRunner

def null_task( n ):
    '''
        expect Task(s) to receive a range list variable "n" which represents
        the n-th iteration they are working on. this can be used ( or not 0
        in the code you are benchmarking
    '''
    # O( n )
    for i in n: pass


def pop_end_task( n ):
    '''
        expect Task(s) to receive a range list variable "n" which represents
        the n-th iteration they are working on. this can be used ( or not 0
        in the code you are benchmarking
    '''
    # O( 1 )
    n.pop()


def pop_index_task( n ):
    '''
        expect Task(s) to receive a range list variable "n" which represents
        the n-th iteration they are working on. this can be used ( or not 0
        in the code you are benchmarking
    '''
    # O( n )
    if len( n ) >= 1:
        n.pop( 25 % len( n ) )


#
#  ARGS: fn, start_range=0, stop_range=5000000, step=20000, graph_label='test', number_of_workers=2 ):
#
#runner1 = TaskRunner( null_task, start_range=0, stop_range=5000000, step=250000, graph_label='foreach pass', number_of_workers=16 )
#runner2 = TaskRunner( pop_end_task, start_range=0, stop_range=2000000, step=1000, graph_label='n.pop()', number_of_workers=16 )
runner3 = TaskRunner( pop_index_task, start_range=0, stop_range=1000000, step=1000, graph_label='n.pop(indx)', number_of_workers=16 )

#
#  WARNING: don't run all of these at once unless you want
#  to kill your computer
#
#runner1()
#runner2()
runner3()
    

