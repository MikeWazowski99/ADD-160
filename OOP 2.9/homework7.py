'''
Homework7
Name: Michael Tapia
github link: https://github.com/MikeWazowski99/ADD-160/tree/main
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Queue:
    def __init__(self,lst=[]): 
        self.q = list(lst)
        pass

    def __repr__(self):
        return f"Queue({self.q})"
        pass

    def enqueue(self,item): 
        #since the list in the init is an array we can just add it the array using append
        self.q.append(item)
        pass

    def dequeue(self): 
        #removes and returns the first item from the queue unless it is empty
        if len(self.q) == 0:
            raise IndexError("Cannot dequeue from empty queue")
        return self.q.pop(0)
        pass

    def __getitem__(self,index):
        if isinstance(index, slice):
            return self.q[index]
        return self.q[index]
        pass

    def __len__(self): # gets current length of the queue
        return len(self.q)
        pass

    def __eq__(self,other):
        if not isinstance(other, Queue):
            return False
        return self.q == other.q
        pass
    def __add__(self,other):
        #Joins two queues into a new queue unless the values that are being added are not both queues
        if not isinstance(other, Queue):
            raise TypeError("Can only add Queue to another Queue")
        return Queue(self.q + other.q)
        pass


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest7.py'))

