# Python Program to find common items from two lists
# using intersection function

# make two lists

def common_items(a, b):
    a = set(a)
    b = set(b)

    # check length
    if len(a.intersection(b)) > 0:
        return("List 1 & 2 common items: ", a.intersection(b))
    else:
        return("List 1 & 2 having no common items.")

# a = [10, 20, 30, 40, 50]
# b = [20, 40, 60, 80, 100]

# common items of given input lists

num = int(input("Enter number of List 1 integer items: "))
a = []
b = []

for i in range(0, num):
    c = int(input(f"Enter List 1 integer item {i}: "))
    a.append(c)

print("List 1: ", a)

for i in range(0, num):
    c = int(input(f"Enter List 2 integer item {i}: "))
    b.append(c)

print("List 2: ", b)
print(common_items(a, b))

# you can also define separately num for b list

# Thanks for Watching