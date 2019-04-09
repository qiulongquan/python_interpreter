s = open('demo.py').read()
# print(s)
co = compile(s, 'demo.py', 'exec')
import dis
dis.dis(co)


# def f(a, b):
#     c = len(a)
#     d = list(range(3))
#     a + b
#
# import dis
# dis.dis(f)


# Python 字节码解释器的工作原理是按照指令的顺序一条一条地顺序执行，
# Python 内部维护着一个数值，这个数值就是 Python 内部的时钟，
# 如果这个数值为 N，则意味着 Python 在执行了 N 条指令以后应该立即启动线程调度机制，
# 可以通过下面的代码获取这个数值。

# 由于 GIL 的存在，Python 的多线程性能十分低下，无法发挥多核 CPU 的优势，性能甚至不如单线程。
# 因此如果你想用到多核 CPU，一个建议是使用多进程。

# import sys
# print(sys.getcheckinterval())  # 100
