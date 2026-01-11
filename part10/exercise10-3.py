guest = input("Enter your name: ")

with open("guest_book.txt", "a") as file:
    file.write(guest + "\n")