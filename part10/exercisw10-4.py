filename = "guest_book.txt"
flag = True

while flag:
    print("Enter 'q' at any time to quit.")
    guest = input("Enter your name: ")
    if guest == "q":
        flag = False
    else:
        with open(filename, "a") as file:
            file.write(guest + "\n")
