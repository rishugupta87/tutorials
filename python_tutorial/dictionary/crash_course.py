# ===============================
# DICTIONARY CRASH COURSE
# ===============================

x = {'key1': 123, 'key2': 456, 'key3': 789}
print("Original:", x)

# Access
print("get key1:", x.get('key1'))
print("index key2:", x['key2'])

# Membership
print("key1 in dict?", 'key1' in x)

# Update
x['key4'] = 999
print("After update:", x)

# Iteration
print("Items:")
for key, value in x.items():
    print(key, value)

print("Keys only:")
for key in x:
    print(key)

print("Values only:")
for val in x.values():
    print(val)

# Comprehension
y = {k: v*2 for k, v in x.items()}
print("Doubled:", y)

# Frequency example
data = ['a', 'b', 'a', 'c', 'b', 'a']
freq = {}
for item in data:
    freq[item] = freq.get(item, 0) + 1
print("Frequency:", freq)
