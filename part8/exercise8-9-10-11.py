def show_messages(messages):
    """打印每条消息"""
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """将每条消息都移到sent_messages中"""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


messages = ["hello world", "how are you", "goodbye"]
sent_messages = []
# 调用函数时,将原始列表的副本传递给函数

send_messages(messages[:], sent_messages)
print("\nFinal lists:")
show_messages(messages)
show_messages(sent_messages)
