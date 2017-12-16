"""
file: linked_code.py
language: python3
author: A. Nunes-Harwitt
author: RIT CS Dept.
description:
   lecture code for data type, and length and reversal functions
   using linked structures with the rit_lib module.

   ################################################
   Data type definition

   A Linked Node Sequence is either
   - None, representing the Empty Linked Sequence, or
   - a Node, which consists of
             * value, and
             * rest, which is a Linked Node Sequence

   The notation Linked(T) refers to the
   Linked Node Sequence type, where T is the type of
   values.
   ################################################

   The value is declared to be object type to support any type of value.
"""

from rit_lib import *

##################################
# Linked Sequence Data Definition
##################################

Node = struct_type("Node"
                , (object, 'value')
                , ((NoneType, "Node"), 'rest'))


##########################
# Recursive length
##########################

def lengthRec(lnk):
    """ lengthRec: Linked(T) -> NatNum
    Compute the length of lnk recursively.
    """
    if lnk == None:
        return 0
    else:
        return 1 + lengthRec(lnk.rest)


####################
# Concatenation cat
####################

def cat(lnk, lnk2):
    """ cat: Linked(T) * Linked(T) -> Linked(T)
    Compute concatenation of lnk and lnk2.
    """
    if lnk == None:
        return lnk2
    else:
        return Node(lnk.value, cat(lnk.rest, lnk2))


###############################
# Recursive reverse
###############################

def reverseRec(lnk):
    """ reverseRec: Linked(T) -> Linked(T)
    Compute reverse of lnk recursively.
    """
    if lnk == None:
        return None
    else:
        return cat(reverseRec(lnk.rest), Node(lnk.value, None))

#############################################################################
# Accumulative Recursion
#############################################################################

################################################
# Accumulative length and tail recursive length
################################################

def lengthAcc(lnk, acc):
    """ lengthAcc: Linked(T) * NatNum -> NatNum
    Compute length of lnk + acc.
    """
    if lnk == None:
        return acc
    else:
        return lengthAcc(lnk.rest, acc + 1)


def lengthTailRec(lnk):
    """ lengthTailRec: Linked(T) -> NatNum
    Compute length of lnk tail recursively.
    """
    return lengthAcc(lnk, 0)


################################################
# Iterative length: derived Iterative form
################################################

def lengthIter(lnk):
    """ lengthIter: Linked(T) -> NatNum
    Compute length of lnk iteratively.
    """
    acc = 0
    while not (lnk == None):
        lnk = lnk.rest  
        acc = acc + 1
    return acc


##################################################
# Accumulative Reverse and tail recursive reverse
##################################################

def reverseAcc(lnk, acc):
    """ reverseAcc: Linked(T) * Linked(T) -> Linked(T)
    Compute reverse of lnk and acc with accumulator.
    """
    if lnk == None:
       return acc
    else:
       return reverseAcc(lnk.rest, Node(lnk.value, acc))


def reverseTailRec(lnk):
    """ reverseTailRec: Linked(T) -> Linked(T)
    Compute tail recursive reverse of lnk.
    """
    return reverseAcc(lnk, None)


################################################
# Iterative reverse: derived Iterative form
################################################

def reverseIter(lnk):
    """ reverseIter: Linked(T) -> Linked(T)
    Compute reverse of lnk iteratively.
    """
    acc = None
    while not (lnk == None):
        acc = Node(lnk.value, acc)
        lnk = lnk.rest
    return acc


#############################
# Accumulative Concatenation
#############################

def catAccum(lnk, lnk2):
    """ cat: Linked(T) * Linked(T) -> Linked(T)
    Compute cat of lnk and lnk2 using lnk2 as an accumulator.
    """
    # double reverse puts things in order!
    return reverseAcc(reverseTailRec(lnk), lnk2)


###########
# InsertAt
###########

def insertAt(index, val, lnk):
    """ insertAt: NatNum * T * Linked(T) -> Linked(T)
    Compute insertion of value at index of lnk.
    """
    if index == 0:
        return Node(val, lnk)
    elif lnk != None:
        return Node(lnk.value, insertAt(index-1, val, lnk.rest))
    else:
        raise IndexError("index out of bounds in insertAt") 


###########
# RemoveAt
###########

def removeAt(index, lnk):
    """ removeAt: NatNum * Linked(T) -> Linked(T)
    Compute removal of value at index from lnk.
    """
    if lnk == None:
        raise IndexError("index out of bounds in removeAt") 
    elif index == 0:
        return lnk.rest
    else:
        return Node(lnk.value, removeAt(index-1, lnk.rest))


#########
# Remove
#########

def remove(val, lnk):
    """ remove: T * Linked(T) -> Linked(T)
    Compute removal of value from lnk.
    """
    if lnk == None:
        return None
    elif lnk.value == val:
        return lnk.rest
    else:
        return Node(lnk.value, remove(val, lnk.rest))


############
# Run tests
############

if __name__ == "__main__": # run tests for this module.

    import test_linked_code as tst
    tst.testLengthRec()
    tst.testCat()
    tst.testReverseRec()
    tst.testLengthAcc()
    tst.testLengthTailRec()
    tst.testLengthIter()
    tst.testReverseAcc()
    tst.testReverseTailRec()
    tst.testReverseIter()
    tst.testCatAccum()
    tst.testInsertAt()
    tst.testRemoveAt()
    tst.testRemove()

