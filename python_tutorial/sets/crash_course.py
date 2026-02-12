x = {1,10,3,3,4,20}
print(x)
y = set()
print("empty set", y)
y.add(10)
y.add(20)
y.remove(10)
print(y)
print(10 in y)
print(20 in y)
print(x.union(y))
print(x.intersection(y))

# iterate over the set
# Basic iteration
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)  # Order not guaranteed!

# With enumerate (if you need a counter)
for i, item in enumerate(my_set):
    print(f"{i}: {item}")

# You can also convert to sorted list first
for item in sorted(my_set):
    print(item)  # Now in order: 1, 2, 3, 4, 5

# Key thing to remember: Sets don't maintain order (though in Python 3.7+ they're somewhat predictable based on insertion), so if order matters, either:
#
# Sort it first: sorted(my_set)
# Use a list instead
# Or if you need both uniqueness AND order, check out dict.fromkeys(items) as a trick (dicts maintain insertion order in Python 3.7+)


# using list comprehension
new_set = {num*2 for num in my_set if num%2==0}
print(new_set)