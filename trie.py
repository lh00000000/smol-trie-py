"""pure python trie / prefix tree implementation"""

DATA = '_DATA_'


def add(root, word):
    working = root
    for c in word:
        if c not in working:
            working[c] = {}
        working = working[c]
    working[DATA] = word


def at(root, prefix):
    if prefix and root:
        return at(root.get(prefix[0], {}), prefix[1:])
    else:
        return root


def items(root):
    if DATA in root:
        yield root[DATA]
    for char, sub_tree in root.items():
        if char is not DATA:
            yield from items(sub_tree)

