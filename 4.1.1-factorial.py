def factorial(n):
    """阶乘函数"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)