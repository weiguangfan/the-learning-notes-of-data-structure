"""
Algorithm DiskUsage(path):
    Input: A string designating a path to a file-system entry
    Output: The cumulative disk space used by that entry and any nested entries
    total = size(path)  {immediate disk space used by the entry}
    if path represents a directory then
        for each child entry stored within directory path do
            total = total + DisUsage(child)  {recursive call}
    return total
"""
import os


def disk_usage(path):
    """
    计算磁盘空间使用情况的递归函数
    分析所执行的递归调用的总数
    这些调用中执行的操作次数
    有O(n)个递归调用，
    并且每个调用运行的时间是O(n),
    从而导致总的运行时间为O(n**2)
    """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path,filename)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total),path)
    return total