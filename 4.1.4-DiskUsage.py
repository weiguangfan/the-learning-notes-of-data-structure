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
    """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path,filename)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total),path)
    return total