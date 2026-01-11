destinations = ["Paris", "New York", "Tokyo", "Sydney", "Rio de Janeiro"]
print("Original order:")
print(destinations)

print("\nHere is the sorted list:")
print(sorted(destinations))

print("\nHere is the original list again:")
print(destinations)

print("\nHere is the reverse list, This is no revers sort list:")
destinations.reverse()
print(destinations)

print("\nUsing reverse(), Here is the reverse list again:")
destinations.reverse()
print(destinations)

print("\nUsing sort(), Here is the sort list again:")
destinations.sort()
print(destinations)

print("\nUsing sort(reverse=True), Here is the revers sort list again:")
destinations.sort(reverse=True)
print(destinations)

# print(destinations[5])
