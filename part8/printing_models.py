def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计,直到没有未打印的设计为止。
    打印每个设计后,都将其移动到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []
print_models(unprinted_designs[:], completed_models)
# 切片表示法[:]创建列表的副本,
# 这样print_models()将原来的列表unprinted_designs的副本传递给它,
show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)
