import math

items = int(input(f"Please enter the number of items: "))
box = int(input(f"Please enter the number of items per box: "))

num_box = math.ceil(items / box)
print()

print(f"For {items} items, packing {box} items in each box, you will need {num_box} boxes.")