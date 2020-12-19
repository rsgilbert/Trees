from lib.Tree import Tree
from lib.EulerTour import EulerTour


# Generating table of comments in O(n) time

# Generate tuples for table of content
def toc(tree, pos=None, depth=0):
    '''Generates information to create table of content i.e. position and depth at that position'''
    if not pos:
        pos = tree.root()
    yield (pos, depth)
    for position in tree.children(pos):
        for yielded_value in toc(tree, position, depth + 1):
            yield yielded_value


def toc_with_index(tree, S=list(), pos=None, depth=0):
    '''Info to create table of content. Includes position, depth, and index'''
    if not pos:
        pos = tree.root()
    yield (pos, depth, indexize(S))
    for (idx, position) in enumerate(tree.children(pos)):
        S.append(idx + 1)
        for yielded_value in toc_with_index(tree, S, position, depth + 1):
            yield yielded_value
        S.pop()



def indexize(S):
    index = '.'.join(str(idx) for idx in S) + " "
    return index 

class TocEulerTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(f'{" " * 2 * d}{indexize(path)} {p.element()}')

