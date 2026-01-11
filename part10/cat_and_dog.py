filenames = ["cat.txt", "dog.txt"]
for filename in filenames:
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        for line in contents.split("\n"):
            print(line)