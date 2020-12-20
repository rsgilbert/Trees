# representing a tree using parenthesis
from lib.EulerTour import EulerTour

def _parenthesize(tree, p):
    '''Uses preorder traversal to print tree elements with parenthesis'''
    print(p.element(), end='')

    if not tree.is_leaf(p):
        print('(', end='')
        for (i, c) in enumerate(tree.children(p)):  
            if i != 0:
                print(', ', end='')         
            _parenthesize(tree, c)
        print(')', end='')


def parenthesize(tree):
    return _parenthesize(tree, tree.root())


class ParenthesisEulerTour(EulerTour):
    '''Create Parenthesis representation of tree using EulerTour implementation'''
    def _hook_previsit(self, p, d, path):
        if len(path) > 0 and path[-1] != 0:
            print_no_newline(', ')
        print_no_newline(p.element())
        if not self._tree.is_leaf(p):
            print_no_newline('(')


    def _hook_postvisit(self, p, d, path, results):
        if not self._tree.is_leaf(p):
            print_no_newline(')')

        



def print_no_newline(x): print(x, end='')