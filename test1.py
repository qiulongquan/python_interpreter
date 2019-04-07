# 列表单元格里面的子项，如何获取值
a=[[1,2],[3,4],[5,6]]
for b in a:
    # 得到指令和对应参数
    # 每个列表的单元 b=[1,2]
    # 通过这个方式拆分开  instruction, argument = b
    # instruction=1
    # argument=2
    instruction, argument = b
    print("instruction={},argument={}".format(instruction,argument))