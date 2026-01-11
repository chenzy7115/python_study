names = ["Alice", "Bob", "Charlie", "David", "Eve"]
for name in names:
    print(f"Hello, {name}! Would you like to join us for dinner?")
no_join = names.pop(2)
print(f"{no_join} can't join us for dinner.")

names.insert(2, "Frank")
print(f"Hello, {names[2]}! Would you like to join us for dinner?")