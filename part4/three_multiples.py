numbers = list(range(1,11))
three_multiples = []
print(f"Here are the numbers,their three multiples: from 1 to 10")
for number in numbers:
    print(number*3,end=' ')
    three_multiples.append(number*3)
print("\nHere is a list of three multiples:")
print(f"{three_multiples}")