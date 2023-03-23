"""
三集不相交
"""


def disjoint1(A,B,C):
    """运行时间O(n**3)"""
    for a in A:  # O(n)
        for b in B:  # O(n)
            for c in C:  # O(n)
                if a == b == c:
                    return False
    return True


def disjoint2(A,B,C):
    """运行时间O(n**2)"""
    for a in A:  # O(n)
        for b in B:  # O(n)
            if a == b:  # 最多n对
                for c in C:  # O(n)
                    if a == c:
                        return False
    return True









