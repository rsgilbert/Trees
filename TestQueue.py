from lib.LinkedQueue import LinkedQueue


q = LinkedQueue()
q.enqueue(20)
q.enqueue(15)
print('len: ', len(q))
print('front: ', q.front())
print('dequeud:', q.dequeue())
print('len: ', len(q))
print('front: ', q.front())
print('dequeued: ', q.dequeue())
# q.dequeue() # we expect an error