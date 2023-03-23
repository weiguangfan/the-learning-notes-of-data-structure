"""
找最大数算法（即计算一系列数中的最大数）的运行时间为O(n)

data[0]的初始运行时间为O(1)
循环执行n次，每次都执行一次比较，赋值，运行时间为O(n)
返回语句机制运行时间为O(1)
综上，算法find_max的运行时间为O(n)

基于随机序列，该算法的最大值被更新的预期次数是O(log n)
"""


def find_max(data):
    """返回列表最大值的函数"""
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest
