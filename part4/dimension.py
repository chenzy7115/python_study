dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# dimensions[0] = 250 # 报错，元组不能修改元素值

# 遍历元组中的所有值
for dimension in dimensions:
    print(dimension)
    
# 修改元组变量
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)