"""递归算法的不足"""


def uinique3(S,start,stop):
    """
    元素唯一性问题
    总的运行时间将正比于递归调用的总数
    n表所考虑的条目总数，即 n = stop - start
    n=1,运行时间为O(1),不进行递归调用

    """
    # at most one item
    if stop - start <= 1:  # O(1)
        return True
    # first part has duplicate
    elif not uinique3(S,start,stop-1):
        return False
    # second part has duplicate
    elif not uinique3(S,start+1,stop):
        return False
    # do first and last differ?
    else:
        return S[start] != S[stop-1]