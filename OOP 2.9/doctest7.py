# queuesTEST.py

##### Queue description #####

Queue class is used for representing a
queue (line) of objects.

Objects are enqueued (added) to the back
of the queue and dequeued (removed) from
the front.

FIFO - first in first out

Our Queue class will be BASED on the list
class, in fact we will do TWO different
IMPLEMENTATIONS.

    Queue_comp - COMPOSITION - build from
    ground up

    Queue_inherit - INHERITANCE - modify
    another class (list)

##### Queue TEST code #####

# test composition
>>> from homework7 import *

# test inheritance
# >>> from Queue_inherit import *

# enqueue, dequeue
>>> q = Queue()  # default constructor
>>> q.enqueue('Mary')
>>> q.enqueue('Fred')
>>> q.enqueue('Alice')
>>> q
Queue(['Mary', 'Fred', 'Alice'])
>>> nowserving = q.dequeue()
>>> nowserving
'Mary'
>>> q
Queue(['Fred', 'Alice'])

# parameterized constructor
>>> qq = Queue([1,2,3])
>>> qq
Queue([1, 2, 3])

# indexing
>>> q[1]  # __getitem__
'Alice'
>>> q[1] = 'Sally' #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
TypeError: bad code: no cutting!

>>> len(q)   # __len__
2

# equals
>>> Queue([1,2,3])==Queue([1,2,3])  # __eq__
True

# iterate
>>> [person for person in q]
['Fred', 'Alice']

# in
>>> 2 in  Queue([1,2,3])
True
>>> 5 in  Queue([1,2,3])
False

# +   ->  __add___
>>> Queue([1,2]) + Queue([3,4])
Queue([1, 2, 3, 4])