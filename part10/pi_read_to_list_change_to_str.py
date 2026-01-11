filename = "pi_digits.txt"

# 打开文件，读取全部内容，存储为list
with open(filename) as file_object:
    lines = file_object.readlines()

print("使用readlines()方法读取文件内容：")
print(lines)
print("list的item: ", end="")
print(len(lines))
# 遍历list，将每一行转换为字符串，并打印
# 使用rstrip()方法去除每行末尾的换行符
print("使用rstrip()方法去除每行末尾的换行符：")

pi_string = ""
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print("字符串长度：", end="")
print(len(pi_string))

# 使用strip()方法去除字符串两端的空格
print("使用strip()方法去除字符串两端的空格：")
pi_string = ""
for line in lines:
    pi_string += line.strip()
print(pi_string)
print("字符串长度：", end="")
print(len(pi_string))
