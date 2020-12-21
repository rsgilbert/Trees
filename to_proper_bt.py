from lib.BinaryTree import BinaryTree


def to_proper_bt(tree, p):
    ''' Convert tree to proper tree
    Use postorder traversal '''

    for c in tree.children(p):
        to_proper_bt(tree, c)
    
    
    if  p != tree.root():
        parent = tree.parent(p)
        if tree.num_children(parent) == 1:
            if tree.left(parent) == p:
                # There is no right position, so we set it to a position with no element
                # print(f'right: {parent.element()}')
                tree._add_right(parent, None)
                # print(f'NOW: right: {tree.right(parent).element()}')
            else:
                # We don't have a left position, so we set it left to a position with no element
                # print(f'left: {parent.element()}')
                tree._add_left(parent, None)
                # print(f'NOW: Left: {tree.left(parent).element()}')
            



        