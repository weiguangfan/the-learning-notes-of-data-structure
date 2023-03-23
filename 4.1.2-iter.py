"""
绘制英式标尺
1 in = 2.54cm
用一个数字标签做上刻度标记，
主刻度线的长度需要指定一个英寸，
整个英寸刻度之间，标尺包含一系列较小的刻度线，
当间隔的大小减少了一半时，刻度线的长度也减1.

中央刻度线长度L>=1的刻度间隔的组成如下：
一个中央刻度线长度为L - 1的刻度间隔
一个长度为L的单独的刻度线
一个中央刻度线长度为L - 1的刻度间隔
"""


def draw_line(tick_length,tick_label=''):
    """
    用指定数量的破折号绘制一个单独的刻度线
    （并且在刻度线之后打印一个可选的字符串标签）
    """
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    """
    根据刻度间隔中中央刻度线的长度来绘制刻度间隔之间副刻度线的序列。
    考虑共有多少行输出；
    输出的每一行是基于一个对draw_line函数的调用，
    以及对draw_interval的每次非零参数递归调用恰好产生的一个对draw_line的直接调用；
    对于c>=0,调用draw_interval(c)函数刚好产生2**c - 1行输出；

    通过调用draw_interval(c)函数打印的行数,
    比通过调用draw_interval(c-1)函数产生的行数的两倍还多1，
    因为在两个这样的递归调用之间打印一个中心线。

    间隔线，画三条线，长度分别是L-1,L,L-1
    """
    if center_length > 0:
        draw_interval(center_length -1)
        draw_line(center_length)
        draw_interval(center_length -1)


def draw_ruler(num_inches,major_length):
    """
    管理整个标尺的构建，
    它的参数指定标尺的总长度以及主刻度线的长度，
    画主刻度线和间隔线
    """
    draw_line(major_length,'0')  # 先画一条
    for j in range(1,1+num_inches):  # 主刻度线画num_inches条
        draw_interval(major_length - 1)
        draw_line(major_length,str(j))  # 数字从1开始