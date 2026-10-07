"""Homework 5: Mutation."""


from __future__ import annotations
from link import Link, LinkedList
from tree import Tree, is_leaf


passphrase = 'REPLACE_THIS_WITH_PASSPHRASE'

def midsem_survey(p):
    """You do not need to understand this code.

    >>> midsem_survey(passphrase)
    '2bf925d47c03503d3ebe5a6fc12d479b8d12f14c0494b43deba963a0'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()


def deep_map(f, s: list) -> None:
    """Replace all non-list elements x with f(x) in the nested list s.

    >>> six = [1, 2, [3, [4], 5], 6]
    >>> deep_map(lambda x: x * x, six)
    >>> six
    [1, 4, [9, [16], 25], 36]
    >>> # Check that you're not making new lists
    >>> s = [3, [1, [4, [1]]]]
    >>> s1 = s[1]
    >>> s2 = s1[1]
    >>> s3 = s2[1]
    >>> deep_map(lambda x: x + 1, s)
    >>> s
    [4, [2, [5, [2]]]]
    >>> s1 is s[1]
    True
    >>> s2 is s1[1]
    True
    >>> s3 is s2[1]
    True
    """
    "*** YOUR CODE HERE ***"


def deep_map_mut(func, s: LinkedList) -> None:
    """Mutates a deep link s by replacing each item found with the
    result of calling func on the item. Does NOT create new Links (so
    no use of Link's constructor).

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> square = lambda x: x * x
    >>> print(link1)
    (3 (4) 5 6)
    >>> link2 = Link(1, Link(Link(Link(2, Link(3))), Link(4)))
    >>> double = lambda x: x * 2
    >>> print(link2)
    (1 ((2 3)) 4)
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not create any new Links."), Link.__init__
    >>> try:
    ...     deep_map_mut(square, link1)
    ...     deep_map_mut(double, link2)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    (9 (16) 25 36)
    >>> print(link2)
    (2 ((4 6)) 8)
    """
    "*** YOUR CODE HERE ***"


def prune_small(t: Tree[int], n: int) -> None:
    """Prune the tree t in place, keeping only the n branches of each node
    with the smallest labels.

    >>> t1 = Tree(6)
    >>> prune_small(t1, 2)
    >>> print(t1)
    6
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_small(t2, 1)
    >>> print(t2)
    6
      3
    >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_small(t3, 2)
    >>> print(t3)
    6
      1
      3
        1
        2
    """
    while ____:
        largest = max(____, key=____)
        ____
    for b in t.branches:
        ____


def delete[T](t: Tree[T], x: T) -> None:
    """Remove all nodes labeled x below the root within Tree t. When a non-leaf
    node is deleted, the deleted node's children become children of its parent.

    The root node will never be removed.

    >>> t = Tree(3, [Tree(2, [Tree(2), Tree(2)]), Tree(2), Tree(2, [Tree(2, [Tree(2), Tree(2)])])])
    >>> delete(t, 2)
    >>> print(t)
    3
    >>> t = Tree(1, [Tree(2, [Tree(4, [Tree(2)]), Tree(5)]), Tree(3, [Tree(6), Tree(2)]), Tree(4)])
    >>> delete(t, 2)
    >>> print(t)
    1
      4
      5
      3
        6
      4
    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(2)]), Tree(2, [Tree(6), Tree(2), Tree(7), Tree(8)]), Tree(4)])
    >>> delete(t, 2)
    >>> print(t)
    1
      4
      5
      3
        6
      6
      7
      8
      4
    """
    new_branches = []
    for _________ in ________________:
        _______________________
        if b.label == x:
            __________________________________
        else:
            __________________________________
    t.branches = ___________________
