names = ["Alice", "Bob", "Charlie", "David", "Eve"]
for name in names:
    print(f"Hello, {name}! Would you like to join us for dinner?")
no_join = names.pop(2)
print(f"{no_join} can't join us for dinner.")

names.insert(2, "Frank")
print(f"Hello, {names[2]}! Would you like to join us for dinner?")

print("\nI found a bigger dinner table!")
names.insert(0, "Grace")
names.insert(3, "Hannah")
names.append("Ivy")

print("New invitations:")
for name in names:
    print(f"Hello, {name}! Would you like to join us for dinner?")
