```

谈谈 Python 程序的运行原理
用简单的例子讲解python的编译和运行原理
https://www.restran.net/2015/10/22/how-python-code-run/

实现解释器需要的基本知识。
通过Python的dis库查看真实的Python字节码，
进一步理解Python解释器的内部机制。

最终参考Byterun（一个现有的Python解释器）
实现一个500行以内的Python解释器。


这个程序实现的解释器只完成最后一部分执行字节码的工作，
也就相当于一个跑Python字节码的Python虚拟机。


Python 字节码解释器的工作原理是按照指令的顺序一条一条地顺序执行，
Python 内部维护着一个数值，这个数值就是 Python 内部的时钟，
如果这个数值为 N，则意味着 Python 在执行了 N 条指令以后应该立即启动线程调度机制，
可以通过下面的代码获取这个数值。

由于 GIL 的存在，Python 的多线程性能十分低下，无法发挥多核 CPU 的优势，性能甚至不如单线程。
因此如果你想用到多核 CPU，一个建议是使用多进程。

import sys
print(sys.getcheckinterval())  # 100

```