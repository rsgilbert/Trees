# Computing diskspace using postorder traversal

import os

def space_usage_iter(path, size=0):
    if is_dir(path):
        for p in list_dir(path):
            for yielded_value in space_usage_iter(joinpath(path, p), size + immediate_size(p)):
                yield yielded_value
    yield size + immediate_size(path)  


def get_pathsize(path):
    size = 0
    for s in space_usage_iter(path):
        size += s
    return size




path = '/'
def immediate_size(path):
    try:
        return os.path.getsize(path)
    except Exception:
        return 0


def is_dir(path):
    return os.path.isdir(path)

def list_dir(path):
    return os.listdir(path)

def joinpath(path1, path2):
    return os.path.join(path1, path2)

mypath = '/home/ssenyonjo/Documents'
size = get_pathsize(mypath)

kilosize = size / 2 ** 10
megasize = kilosize / 2 ** 10
gigasize = megasize / 2 ** 10

print(kilosize)
print(megasize)
print(gigasize)

