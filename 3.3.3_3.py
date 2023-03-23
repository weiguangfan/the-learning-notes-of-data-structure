"""
元素唯一性
以排序作为解决问题的工具
"""


def unique1(S):
    """运行时间O(n**2)"""
    for j in range(len(S)):  # O(n)
        for k in range(j+1,len(S)):  # (n-1) + (n-2) +... + 1 ,O(n**2)
            if S[j] == S[k]:
                return False
    return True  # O(1)


def unique2(S):
    temp = sorted(S)
    for j in range(1,len(temp)):
        if temp[j-1] == temp[j]:
            return False
    return True





