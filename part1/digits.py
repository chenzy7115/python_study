print("Here are the numbers from 1 to 0:")
digits = list(range(1, 10))
digits.append(0)
print(digits)

print("\nMinimum value:")
print(min(digits))

print("\nMaximum value:")
print(max(digits))

print("\nSum of values:")
print(sum(digits))

print("\nHere is using list comprehension:")
squares = [value**2 for value in range(1, 11)]
print(squares)