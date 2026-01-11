# motocycles = ['honda', 'yamaha', 'suzuki']
# print(motocycles)

# # motocycles[0] = 'ducati'
# # print(motocycles)

# motocycles.append('ducati')
# print(motocycles)

motocycles = []

motocycles.append("honda")
motocycles.append("yamaha")
motocycles.append("suzuki")

print(motocycles)

motocycles.insert(0, "ducati")

print(motocycles)

print("\nUsing del to remove an item by index:")

del motocycles[0]

print(motocycles)

print("\nUsing pop() to remove an item by index:")

popped_motocycle = motocycles.pop()

print(motocycles)
print(popped_motocycle)


first_owned = motocycles.pop(0)
print(f"\nThe first motocycle I owned was a {first_owned.title()}.")

motocycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocycles)

too_expensive = 'ducati'
motocycles.remove(too_expensive)
print(motocycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

