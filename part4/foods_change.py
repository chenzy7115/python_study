# 这里说明list实际上对象，List name 是指向List的引用，所以当你用List name 赋值给另一个变量时，实际上是将引用复制给了新变量，而不是复制了List本身。这意味着，当你修改其中一个变量时，另一个变量也会受到影响。
# 要复制List本身，你可以使用切片操作符[:]，这将创建一个新的List，其中包含与原始List相同的元素。这样，当你修改一个变量时，另一个变量不会受到影响。
# python中的对象，包括list，dict，set，tuple等都是对象，对象是内存中的一块区域，存储了数据和方法。
# 当你将一个对象赋值给另一个变量时，实际上是将变量指向了对象的内存地址。这意味着，当你修改其中一个变量时，另一个变量也会受到影响。
# 比较C语言中的指针，C语言中的指针是指向内存地址的变量，当你将一个指针赋值给另一个指针时，实际上是将指针指向了同一个内存地址。这意味着，当你修改其中一个指针时，另一个指针也会受到影响。
# 所以，在Python中，当你将一个对象赋值给另一个变量时，实际上是将变量指向了对象的内存地址。当你修改其中一个变量时，另一个变量也会受到影响。
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
for food in my_foods:
    print(f"{food.title()}, ", end="")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"{food.title()}, ", end="")
