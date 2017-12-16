"""
Queue implementation built on top of nodes.
file: myQueue.py
author: Arthur Nunes-Harwitt

This is Queue datatype implemented by a linked node sequence.
"""

from linked_code import *

Queue = struct_type("Queue",
           (int, 'size'),
           ((NoneType, Node), 'front'), ((NoneType, Node), 'back'))

def mkEmptyQueue():
    """
    Returns a new queue with size initialized to zero and
    the front and back fields initialized to the empty sequence.
    """
    return Queue(0, None, None)

def enqueue(queue, element):
    """
    Insert an element into the back of the queue. (Returns None)
    """
    newnode = Node(element, None)
    if emptyQueue(queue):
        queue.front = newnode
    else:
        queue.back.rest = newnode
    queue.back = newnode
    queue.size = queue.size + 1
    
def dequeue(queue):
    """
    Remove the front element from the queue. (returns None)
    precondition: queue is not empty.
    """
    if emptyQueue(queue):
        raise IndexError("dequeue on empty queue") 
    queue.front = queue.front.rest
    if emptyQueue(queue):
        queue.back = None
    queue.size = queue.size - 1
    
def front(queue):
    """
    Access and return the first element in the queue without removing it.
    precondition: queue is not empty.
    """
    if emptyQueue(queue):
        raise IndexError("front on empty queue") 
    return queue.front.value
    
def back(queue):
    """
    Access and return the last element in the queue without removing it
    precondition: queue is not empty.
    """
    if emptyQueue(queue):
        raise IndexError("back on empty queue") 
    return queue.back.value
    
def emptyQueue(queue):
    """
    Is the queue empty?
    """
    return queue.front == None

