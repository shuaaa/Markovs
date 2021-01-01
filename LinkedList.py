#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 07:56:00 2020

@author: olamijojo
"""
# prints out the namespace dictionary  called locals
print(locals())



# prints memory location of the stored varibles d & j
d = 'Dave'
j = d # j = d implies we just copy d's reference over to j's namespace entry.
print(id(d), id(j))

# changing assignment
# Assignment changes what object a variable refers to, it does not have any 
# effect on the object itself.
#  This process is known as garbage collection. i.e reuse of memory locations
# by reassignment.

j = 'Smith'


# removing mapping from a given name by delete func

del d

# Aliasing

lst1 =[1, 2, 3]
lst2 = lst1
lst2.append(4)
lst1

# Shallow copy & deep copy
# A shallow copy has its own top-level references, but those references 
#refer to the same objects

# deep copy is a completely separate copy that creates both new references 
# and, where necessary, new data objects at all levels

import copy

b = [1, 2,[3 ,4], 6]

c = b
d = copy.copy(b) # creates a shallow copy
e = copy.deepcopy(b) # create a deep copy

print(b is c, b == c)

print(b is d, b == c)

print(b is c, b == e)


b[0] = 0
b.append(7)
c[2].append(5)
print(b)
print(c)
print(d) # shallow copy does not get the append updates
print(e) # shallow copy does not get the append updates

"""
 Changing the top level of the list referred to by b causes c to change, 
 since it refers to the same object. The top-level changes have no effect 
 on d or e, since they refer to separate objects that are copies of b.
Things get interesting when we change the sublist [3 , 4] through c . 
Of course b sees these changes (since b and c are the same object).
But now d also sees those changes, since this sublist is still a shared 
substructure in the shallow copy.
 
"""

