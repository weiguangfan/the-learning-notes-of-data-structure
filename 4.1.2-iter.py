def draw_line(tick_length,tick_label=''):
    """用指定数量的破折号绘制一个单独的刻度线"""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    """间隔线，画三条线，长度分别是L-1,L,L-1"""
    if center_length > 0:
        draw_interval(center_length -1)
        draw_line(center_length)
        draw_interval(center_length -1)


def draw_ruler(num_inches,major_length):
    """画主刻度线和间隔线"""
    draw_line(major_length,'0')  # 先画一条
    for j in range(1,1+num_inches):  # 主刻度线画num_inches条
        draw_interval(major_length - 1)
        draw_line(major_length,str(j))  # 数字从1开始