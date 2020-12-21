# R-8.5
# An algorithm that counts the number of leaves in a
# binary tree that are the left child of their respective parent


from lib.BinaryTree import BinaryTree


def count_left_leaves(tree, p=None): 
    '''Uses postorder to count left leaves'''
    
    if p is None:    
        return count_left_leaves(tree, tree.root())

    if tree.is_leaf(p):
        parent = tree.parent(p)
        if tree.left(parent) == p:
            # position is a left leaf
            # print('element is ', p.element())
            return 1
        return 0

    left = tree.left(p)
    right = tree.right(p)

    if left and right:
        # Both left and right node exist
        return count_left_leaves(tree, left) + count_left_leaves(tree, right)

    if left:
        # Left node exists but right node does not. So we do not count the right node leaves
        return count_left_leaves(tree, left) 

    if right:
        # Right node exists but left node does not. So we do not count the left node leaves
        return count_left_leaves(tree, right) 

        
    
        
    
