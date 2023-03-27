"""
元素唯一性
以排序作为解决问题的工具
"""


def unique1(S):
    """
    运行时间O(n**2)
    元素和后面的每一个元素比较
    """
    for j in range(len(S)):  # O(n)
        for k in range(j+1,len(S)):  # (n-1) + (n-2) +... + 1 ,O(n**2)
            if S[j] == S[k]:
                return False
    return True  # O(1)


def unique2(S):
    """
    运行时间O(nlog n)
    先排序，
    遍历元素，后一个元素和前一个元素比较
    """
    temp = sorted(S)  # sorted(),O(nlog n)
    for j in range(1,len(temp)):  # 外层，n-1次
        if temp[j-1] == temp[j]:  # O(1),
            return False
    return True





