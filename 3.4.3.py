"""
归纳和循环不变量
"""


def find(S,val):
    """寻找给定元素在列表中第一个出现的索引值"""
    n = len(S)  # O(n)
    j = 0
    while j < n:  # n 次
        if S[j] == val:  # O(1)
            return j
        j += 1
    return -1  # O(1)

            