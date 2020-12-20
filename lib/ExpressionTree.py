from .LinkedBinaryTree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    '''An arithmetic expression tree'''

    def __init__(self, token, left=None, right=None):
        '''Create an ExpressionTree either from a token or from a token and two subtrees'''

        # Inherited Tree has an initialization method that must be called to set it up
        super().__init__()

        if not isinstance(token, str):
            raise TypeError(f'Token must be a string, got  {type(token)}')

        self._add_root(token)

        if left or right:
            if not left or not right:
                raise TypeError("Left or Right can not be None")
            if token not in "*-+/":
                raise ValueError("Token must be one of *, -, +, /")
            self._attach(self.root(), left, right)

    def __str__(self):
        '''Return string representation of expression'''
        S = []
        self._str(self.root(), S)
        return ''.join(S)

    def _str(self, p, S):
        # Pre
        if not self.is_leaf(p):
            S.append('(')

        # We perform Inorder traversal within the brackets
        # Left
        for c in self.children(self.left(p)):
            self._str(c, S)

        # Center
        S.append(p.element())

        # Right
        for c in self.children(self.right(p)):
            self._str(c, S)

        # Inorder traversal has ended
        # Post
        if not self.is_leaf(p):
            S.append(')')

    def evaluate(self):
        return self._evaluate(self.root())

    def _evaluate(self, p):
        '''Use post order to compute value of expression'''
        if not self.is_leaf(p):
            return operate(self._evaluate(self.left(p)), p.element(), self._evaluate(self.right(p)))
        return p.element()

def build_tree(tokens):
    '''Build expression tree from a string of tokens. The tokens must use sigle digit numbers with no spaces'''
    S = []
    for t in tokens:
        if t in '*/-+':
            S.append(t)
        elif t not in '()':
            S.append(ExpressionTree(t))
        elif t == ')':
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op, left, right))
    # The remaining item in S will be the ExpressionTree
    return S.pop()


def operate(lop, op, rop):
    lop, rop = int(lop), int(rop)
    if op == '-':
        return lop - rop
    if op == '+':
        return lop + rop
    if op == '*':
        return lop * rop
    if op == '/':
        return lop / rop
    raise ValueError('Unknown operator')
