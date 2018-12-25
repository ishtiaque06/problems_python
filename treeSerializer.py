"""
>>> node = Node('root', Node('left', Node('left.left')), Node('right'))

>>> serialize(node)

"""


class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    if type(node) == type(Node('1')):
        return (pre_order_serialize(node, []))

    else:
        return

# def deserialize(list):


def pre_order_serialize(node, string):
    if not node:
        string.append(None)
        return string
    string.append(node.val)
    pre_order_serialize(node.left, string)
    pre_order_serialize(node.right, string)

    return string


if __name__ == "__main__":
    import doctest
    doctest.testmod()