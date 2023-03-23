"""
二分查找
用于在一个含有n个元素的有序序列中有效地定位目标值

当序列无序时，循环检查每一个元素，顺序查找算法，运行时间O(n);

在查找时，如果不能排除一个元素与目标值相匹配，那么称序列的这个元素为候选项。
当序列有序并且可通过索引访问时，该算法维持两个参数low和high,
这样可使所有候选条目的索引位于low和high中间。
low = 0 , high = n-1
然后我们比较目标值和中间值候选项，即索引项[mid]的数据。
mid = (low + high)/2
target = data[mid] , 终止；
target < data[mid], 前一半序列重复这一过程，low 到 mid-1;
target > data[mid], 后一半序列重复这一过程，mid+1 到 high;
运行时间O(logn)
"""


def binary_search(data,target,low,high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data,target,low,mid-1)
        elif target > data[mid]:
            return binary_search(data,target,mid+1,high)

