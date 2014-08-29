from zcollections.Stack import Stack
import json
from logger import logger

def traverse_recursive_dict( node ):
    #
    #  assumes we are using 
    #  a data structure
    #  for Node(s) that
    #  are Python core data structures
    #
    if node is None: return

    if isinstance( node, dict ):
        for child_key, child in node.items():
            traverse_recursive_dict( child )
    elif isinstance( node, list ):
        for child in node:
            traverse_recursive_dict( child )
    #logger.debug( "[ NODE ]: %s" % node )


def traverse_recursive( node ):
    #
    #  assumes we are using 
    #  a data structure
    #  for Node(s) that
    #  are Python core data structures
    #
    if node is None: return

    for child in node.children:
        traverse_recursive( child )
    #logger.debug( "[ NODE ]: %s" % node )


def traverse_stack( node ):
    #
    #  assumes we are using 
    #  a data structure
    #  for Node(s) that
    #  has interface for children 
    #  ( and probably parents )
    #
    if node is None: return

    stack = Stack()
    stack.push( node )
    while not stack.is_empty():
        top = stack.pop()
        for child in top.children:
            stack.push( child )


def traverse_dict_stack( node ):
    #
    #  assumes we are using 
    #  a data structure
    #  for Node(s) that
    #  are Python core data structures
    #
    if not node: return

    stack = Stack()
    stack.push( node )
    while not stack.is_empty():
        node = stack.pop()

        if isinstance( node, dict ):
            for child_key, child in node.items():
                stack.push( child )
        elif isinstance( node, list ):
            for child in node:
                stack.push( child )

        #logger.debug( "[ NODE ]: %s" % node )


def traverse_dict( node ):
    #
    #  assumes we are using 
    #  a data structure
    #  for Node(s) that
    #  are Python core data structures
    #
    if not node: return

    nodes = [ node ]
    while nodes:
        node = nodes.pop()

        if isinstance( node, dict ):
            for child_key, child in node.items():
                nodes = [ child ] + nodes
        elif isinstance( node, list ):
            for child in node:
                nodes = [ child ] + nodes

        #logger.debug( "[ NODE ]: %s" % node )

    
if __name__ == '__main__':

    json_data = '{ \
        "name" : "Samuel J" , \
        "servees" : [ \
            "Dykstra", \
            "Tom"  \
        ] , \
        "hash" : { \
            "bank" : true , \
            "sank" : false  \
        } \
    }'

    json_dict = json.loads( json_data )
    #traverse_dict_stack( json_dict )
    traverse_dict( json_dict )

    

