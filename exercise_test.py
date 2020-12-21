from lib.LinkedBinaryTree import LinkedBinaryTree
from left_leaves import count_left_leaves
from to_proper_bt import to_proper_bt




# tests
t = LinkedBinaryTree()
t._add_root(1)
l = t._add_left(t.root(), 2)
r = t._add_right(t.root(), 5)

t._add_right(l, 4)
t._add_left(r, 8)
k = t._add_right(r, 9)
t._add_left(k,15)
t._add_right(k, 20)


# Improper tree
t2 = LinkedBinaryTree()
t2._add_root(1)
l = t2._add_left(t2.root(), 2)
r = t2._add_right(t2.root(), 5)
# t2._add_left(l, 3)
t2._add_right(l, 4)
# t2._add_left(r, 8)
k = t2._add_right(r, 9)
t2._add_left(k,15)
# t2._add_right(k, 20)

'''
        1
       / \\
       2   5
      /\\  / \\
    3   4  8  9
             / \\
            15  20

    Preorder: 1, 2, 3, 4, 5, 8, 9, 15, 20
    Postorder: 3, 4, 2, 8, 15, 20, 9, 5, 1
    Breadthfirst: 1, 2, 5, 3, 4, 8, 9, 15, 20
    Inorder: 3, 2, 4, 1, 8, 5, 15, 9, 20

    toc with indexes:
        1
        1  2
            1.1  3
            1.2  4
        2  5
            2.1  8
            2.2  9
            2.2.1  15
            2.2.2  20

'''

## Test Count left leaves ##
print('\n ## Count left leaves ## \n')

count = 0

print(count_left_leaves(t))


## Test to_proper_bt ##
print('\n ## to_proper_bt ## \n')
print(len(t2))
to_proper_bt(t2, t2.root())
print(len(t2))
