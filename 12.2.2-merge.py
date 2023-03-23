def merge(S1,S2,S):
    """合并两个子列表，并排序"""
    # TODO 分析排序过程
    i = j = 0
    while i+j < len(S):
        if j == len(S2) or (i < len(S1)) and S1[i] < S2[j]:
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1


def merge_sort(S):
    """切分，直到元素个数为1"""
    # TODO 切分完进行合并
    n = len(S)
    if n < 2:
        return
    mid = n//2
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1,S2,S)


def merge_sort2(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # 递归地进行分治操作
    left_arr = merge_sort2(left_arr)
    right_arr = merge_sort2(right_arr)

    # 合并两个有序子序列
    result = []
    i, j = 0, 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1

    result += left_arr[i:]
    result += right_arr[j:]

    return result
