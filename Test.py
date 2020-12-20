from lib.LinkedBinaryTree import LinkedBinaryTree
from toc import toc, toc_with_index, TocEulerTour
from BinaryLayout import BinaryLayout
from parenthesis import parenthesize, ParenthesisEulerTour
from lib.ExpressionTree import ExpressionTree, build_tree

# tests
t = LinkedBinaryTree()
t._add_root(1)
l = t._add_left(t.root(), 2)
r = t._add_right(t.root(), 5)
t._add_left(l, 3)
t._add_right(l, 4)
t._add_left(r, 8)
k = t._add_right(r, 9)
t._add_left(k,15)
t._add_right(k, 20)

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


# Preorder
print('\n## Preorder ##\n')
l = [t._validate(i)._element for i in t.preorder()]
print(l)

# Postorder
print('\n## Postorder ##\n')
l = [t._validate(i)._element for i in t.postorder()]
print(l)


# Breadthfirst
print('\n## Breadthfirst ##\n')
l = [t._validate(i)._element for i in t.breadthfirst()]
print(l)


# Inorder (for binary trees)
print('\n## Inorder ##\n')
l = [t._validate(i)._element for i in t.inorder()]
print(l)


## Table of contents
print('\n## Table of contents ## \n')
for (p, d) in toc(t):
    print('  ' * d, t._validate(p)._element)


## Table of contents with indexes
print('\n## Table of Contents With Indexes ## \n')
for (p, d, index) in toc_with_index(t):
    print('  ' * d, index,  t._validate(p)._element)


## Table of contents with indexes using EulerTour
print('\n## Table of Contents With Indexes Using EulerTour ## \n')
eulertour = TocEulerTour(t)
eulertour.execute()


# Parenthesis
print('\n ## Parenthesis representation of a tree ## \n')
parenthesize(t)

# Parenthesis using EulerTour
print('\n\n## ParenthesisEulerTour ##\n')
parenthesized_tour = ParenthesisEulerTour(t)
parenthesized_tour.execute()

# Binary Layout
print('\n\n ## Binary Layout ## \n')
layout = BinaryLayout(t)
layout.execute()


# ExpressionTree
print('\n ## Expression Tree ## \n')
exp = ExpressionTree('*')


ex_t = build_tree('((8*5)+(3-(4*3)))')
print(ex_t.evaluate())