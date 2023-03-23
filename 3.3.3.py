"""
计算一个序列的前缀平均值
二次-时间算法
线性-时间算法
"""


def prefix_average1(S):
    """运行时间为O(n**2)"""
    n = len(S)  # O(1)
    A = [0]*n  # O(n)
    for j in range(n):  # 外层，n次
        total = 0  # n次，O(n)
        for i in range(j + 1):  # 内层，取决于j
            total += S[i]  # 1+2+...+n，O(n**2)
        A[j] = total/(j+1)  # n次，O(n)
    return A  # O(1)


def prefix_average2(S):
    """运行时间O(n**2)"""
    n = len(S)  # O(1)
    A = [0] * n  # O(n)
    for j in range(n):  # 外层，n-1次
        A[j] = sum(S[0:j+1]) / (j+1)  # sum()函数调用，S[0:j+1]运行时间O(j+1);1+2+...+n
    return A  # O(1)


def prefix_average3(S):
    """运行时间O(n)"""
    n = len(S)  # O(1)
    A = [0]*n  # O(n)
    total = 0  # O(1)
    for j in range(n):  # 外层，n次
        total += S[j]  # O(1),n次
        A[j] = total/(j+1)  # O(1),n次
    return A

