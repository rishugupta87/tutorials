# 🎯 Python Sets Crash Course

Master unique, unordered collections

---

## 1. The Basics

Sets are **unordered** collections of **unique** elements. Perfect for removing duplicates and mathematical set operations.

### Creating Sets

```python
# Empty set (must use set(), not {})
empty = set()  # ✅ Correct
# empty = {}   # ❌ This creates an empty dict!

# With initial values
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14, True}

# From other iterables
from_list = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4}
from_string = set("hello")  # {'h', 'e', 'l', 'o'}
from_range = set(range(5))  # {0, 1, 2, 3, 4}

# Set comprehension
squares = {x**2 for x in range(5)}
# {0, 1, 4, 9, 16}
```

**💡 Key Point:** Sets automatically remove duplicates!

```python
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # {1, 2, 3}
```

---

## 2. Key Characteristics

### Unordered
```python
my_set = {3, 1, 4, 1, 5, 9, 2}
print(my_set)  # Order is unpredictable!
# Might print: {1, 2, 3, 4, 5, 9}
# Or: {9, 1, 2, 3, 4, 5}

# ❌ Can't access by index
# my_set[0]  # TypeError!
```

### No Duplicates
```python
fruits = {"apple", "banana", "apple", "cherry"}
print(fruits)  # {'apple', 'banana', 'cherry'}
```

### Elements Must Be Immutable
```python
# ✅ Works - immutable types
valid = {1, "hello", 3.14, True, (1, 2, 3)}

# ❌ Error - mutable types
# invalid = {[1, 2, 3]}  # TypeError: unhashable type: 'list'
# invalid = {{1: 2}}     # TypeError: unhashable type: 'dict'
```

---

## 3. Adding & Removing Elements

### Adding Elements

```python
fruits = {"apple", "banana"}

# add() - add single element
fruits.add("cherry")
# {'apple', 'banana', 'cherry'}

# Adding duplicate does nothing
fruits.add("apple")
# Still {'apple', 'banana', 'cherry'}

# update() - add multiple elements
fruits.update(["date", "elderberry"])
# {'apple', 'banana', 'cherry', 'date', 'elderberry'}

# update() with another set
fruits.update({"fig", "grape"})

# update() with multiple iterables
fruits.update(["kiwi"], {"lemon"}, ("mango",))
```

### Removing Elements

```python
fruits = {"apple", "banana", "cherry"}

# remove() - raises KeyError if not found
fruits.remove("banana")
# {'apple', 'cherry'}
# fruits.remove("grape")  # ❌ KeyError!

# discard() - no error if not found
fruits.discard("cherry")  # Removes it
fruits.discard("grape")   # Does nothing, no error

# pop() - remove and return arbitrary element
item = fruits.pop()  # Returns 'apple' (or any element)
# Can't pop from empty set - KeyError

# clear() - remove all elements
fruits.clear()  # set()
```

---

## 4. Set Operations (The Power of Sets!)

### Union (|) - All elements from both sets

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using | operator
union = A | B
# {1, 2, 3, 4, 5, 6}

# Using .union() method
union = A.union(B)
# {1, 2, 3, 4, 5, 6}

# Multiple sets
C = {7, 8}
union = A | B | C
# {1, 2, 3, 4, 5, 6, 7, 8}
```

### Intersection (&) - Only common elements

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using & operator
common = A & B
# {3, 4}

# Using .intersection() method
common = A.intersection(B)
# {3, 4}

# Multiple sets
C = {3, 7, 8}
common = A & B & C
# {3}
```

### Difference (-) - Elements in first but not second

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# A - B: elements in A but not in B
diff = A - B
# {1, 2}

# B - A: elements in B but not in A
diff = B - A
# {5, 6}

# Using .difference() method
diff = A.difference(B)
# {1, 2}
```

### Symmetric Difference (^) - Elements in either but not both

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using ^ operator
sym_diff = A ^ B
# {1, 2, 5, 6}

# Using .symmetric_difference() method
sym_diff = A.symmetric_difference(B)
# {1, 2, 5, 6}
```

### Visual Summary

```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A | B  →  {1, 2, 3, 4, 5, 6}     # Union (all)
A & B  →  {3, 4}                  # Intersection (common)
A - B  →  {1, 2}                  # Difference (A only)
B - A  →  {5, 6}                  # Difference (B only)
A ^ B  →  {1, 2, 5, 6}           # Symmetric diff (not common)
```

---

## 5. Set Comparison & Testing

### Subset & Superset

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 3}

# Subset (<=) - all elements of A are in B
A.issubset(B)     # True
A <= B            # True

# Proper subset (<) - subset but not equal
A < B             # True
A < C             # False (they're equal)

# Superset (>=) - A contains all elements of B
B.issuperset(A)   # True
B >= A            # True

# Proper superset (>)
B > A             # True
C > A             # False (they're equal)
```

### Disjoint Sets

```python
A = {1, 2, 3}
B = {4, 5, 6}
C = {3, 4, 5}

# Disjoint - no common elements
A.isdisjoint(B)   # True (no overlap)
A.isdisjoint(C)   # False (3 is common)
```

### Equality

```python
A = {1, 2, 3}
B = {3, 2, 1}  # Order doesn't matter!
C = {1, 2, 3, 3, 3}  # Duplicates removed

A == B  # True
A == C  # True
```

---

## 6. Checking Membership

```python
fruits = {"apple", "banana", "cherry"}

# Check if element exists (FAST - O(1))
if "apple" in fruits:
    print("Found!")

if "grape" not in fruits:
    print("Not found!")

# Length
count = len(fruits)  # 3

# Check if empty
if fruits:
    print("Set has elements")
if not fruits:
    print("Set is empty")
```

**💡 Performance:** Checking membership in sets is **much faster** than lists!

```python
# For large collections, use sets for membership testing
# Set: O(1) - constant time
# List: O(n) - has to check each element
```

---

## 7. Iterating Through Sets

```python
fruits = {"apple", "banana", "cherry"}

# Basic iteration (order unpredictable)
for fruit in fruits:
    print(fruit)

# Can't use enumerate directly (no order/index)
# But can convert to list first
for i, fruit in enumerate(sorted(fruits)):
    print(f"{i}: {fruit}")

# Iterate in sorted order
for fruit in sorted(fruits):
    print(fruit)
# apple
# banana  
# cherry
```

---

## 8. Set Comprehensions

```python
# Basic syntax: {expression for item in iterable}

# Squares
squares = {x**2 for x in range(6)}
# {0, 1, 4, 9, 16, 25}

# With condition
evens = {x for x in range(10) if x % 2 == 0}
# {0, 2, 4, 6, 8}

# From string - unique characters
chars = {c.lower() for c in "Hello World" if c.isalpha()}
# {'h', 'e', 'l', 'o', 'w', 'r', 'd'}

# Extract unique values
users = [
    {'name': 'Alice', 'role': 'admin'},
    {'name': 'Bob', 'role': 'user'},
    {'name': 'Charlie', 'role': 'admin'}
]
roles = {user['role'] for user in users}
# {'admin', 'user'}
```

---

## 9. Frozen Sets (Immutable Sets)

```python
# Regular set - mutable
regular = {1, 2, 3}
regular.add(4)  # ✅ Works

# Frozen set - immutable
frozen = frozenset([1, 2, 3])
# frozen.add(4)  # ❌ AttributeError!

# Use frozen sets as dictionary keys or set elements
valid_dict = {frozenset([1, 2]): "value"}
nested_set = {frozenset([1, 2]), frozenset([3, 4])}

# Same operations as sets (except modification)
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
union = fs1 | fs2  # frozenset({1, 2, 3, 4, 5})
```

---

## 10. Common Patterns & Use Cases

### Remove Duplicates from List

```python
# Preserves uniqueness but loses order
numbers = [1, 2, 2, 3, 1, 4, 3, 5]
unique = list(set(numbers))
# [1, 2, 3, 4, 5] (order not guaranteed)

# Preserve order (Python 3.7+)
unique = list(dict.fromkeys(numbers))
# [1, 2, 3, 4, 5] (order preserved)
```

### Find Common Elements

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Common elements
common = set(list1) & set(list2)
# {4, 5}

# As list
common = list(set(list1) & set(list2))
```

### Find Unique Elements

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Elements only in list1
only_in_1 = set(list1) - set(list2)
# {1, 2, 3}

# Elements only in list2
only_in_2 = set(list2) - set(list1)
# {6, 7, 8}

# Elements in either but not both
unique = set(list1) ^ set(list2)
# {1, 2, 3, 6, 7, 8}
```

### Check for Duplicates

```python
def has_duplicates(items):
    return len(items) != len(set(items))

numbers = [1, 2, 3, 4, 5]
print(has_duplicates(numbers))  # False

numbers = [1, 2, 2, 3]
print(has_duplicates(numbers))  # True
```

### Validate Unique Identifiers

```python
user_ids = [101, 102, 103, 104]
new_id = 105

if new_id not in set(user_ids):
    user_ids.append(new_id)
    print("ID added")
else:
    print("ID already exists")
```

### Filter Items Present in Blacklist

```python
items = ["apple", "banana", "cherry", "date"]
blacklist = {"banana", "date"}

filtered = [item for item in items if item not in blacklist]
# ['apple', 'cherry']

# Or using set difference
filtered = list(set(items) - blacklist)
```

### Track Unique Visitors

```python
visitors = set()

def record_visit(user_id):
    visitors.add(user_id)

def get_unique_count():
    return len(visitors)

record_visit(101)
record_visit(102)
record_visit(101)  # Duplicate
print(get_unique_count())  # 2
```

---

## 11. Set Methods Cheat Sheet

| Method | What It Does | Example |
|--------|-------------|---------|
| `.add(x)` | Add element | `s.add(5)` |
| `.update(iterable)` | Add multiple | `s.update([1,2,3])` |
| `.remove(x)` | Remove (error if missing) | `s.remove(5)` |
| `.discard(x)` | Remove (no error) | `s.discard(5)` |
| `.pop()` | Remove arbitrary element | `x = s.pop()` |
| `.clear()` | Remove all | `s.clear()` |
| `.copy()` | Shallow copy | `new = s.copy()` |
| `.union(other)` | Combine (|) | `s1.union(s2)` |
| `.intersection(other)` | Common (&) | `s1.intersection(s2)` |
| `.difference(other)` | In s1 not s2 (-) | `s1.difference(s2)` |
| `.symmetric_difference(other)` | Not common (^) | `s1.symmetric_difference(s2)` |
| `.issubset(other)` | All in other (<=) | `s1.issubset(s2)` |
| `.issuperset(other)` | Contains all (>=) | `s1.issuperset(s2)` |
| `.isdisjoint(other)` | No common elements | `s1.isdisjoint(s2)` |

---

## 12. Set Operations Summary

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Operations that return new sets
A | B              # Union: {1, 2, 3, 4, 5, 6}
A & B              # Intersection: {3, 4}
A - B              # Difference: {1, 2}
A ^ B              # Symmetric difference: {1, 2, 5, 6}

# Operations that modify original set
A.update(B)                    # A = A | B
A.intersection_update(B)       # A = A & B
A.difference_update(B)         # A = A - B
A.symmetric_difference_update(B) # A = A ^ B
```

---

## 13. When to Use Sets vs Lists

### Use Sets When:
- ✅ You need unique elements
- ✅ Order doesn't matter
- ✅ Fast membership testing (`x in set`)
- ✅ Mathematical set operations
- ✅ Removing duplicates

### Use Lists When:
- ✅ Order matters
- ✅ Duplicates are needed
- ✅ Need indexing/slicing
- ✅ Elements might be mutable

### Performance Comparison

```python
# Membership testing
# Set: O(1) - instant
# List: O(n) - has to search through all elements

# For 1 million items:
big_set = set(range(1000000))
big_list = list(range(1000000))

# Finding if 999999 is present:
# 999999 in big_set   # Nearly instant
# 999999 in big_list  # Checks ~1 million items
```

---

## 14. Common Mistakes

### ❌ Creating Empty Set with {}

```python
# WRONG - creates empty dict
empty = {}
type(empty)  # <class 'dict'>

# CORRECT
empty = set()
type(empty)  # <class 'set'>
```

### ❌ Trying to Add Mutable Elements

```python
# WRONG
my_set = {[1, 2, 3]}  # ❌ TypeError!

# CORRECT - use tuple instead
my_set = {(1, 2, 3)}  # ✅ Works
```

### ❌ Expecting Order

```python
# WRONG - assuming order
my_set = {3, 1, 4, 1, 5}
first = list(my_set)[0]  # Unpredictable!

# CORRECT - sort if you need order
first = sorted(my_set)[0]  # Predictable
```

### ❌ Modifying Set While Iterating

```python
# WRONG
numbers = {1, 2, 3, 4, 5}
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # ❌ RuntimeError!

# CORRECT
numbers = {1, 2, 3, 4, 5}
numbers = {num for num in numbers if num % 2 != 0}
```

---

## 15. Quick Reference

```python
# CREATE
s = set()
s = {1, 2, 3}
s = set([1, 2, 3])
s = {x for x in range(5)}

# ADD/REMOVE
s.add(x)
s.update([1, 2, 3])
s.remove(x)      # Error if missing
s.discard(x)     # No error
s.pop()
s.clear()

# CHECK
x in s
x not in s
len(s)
s.issubset(other)
s.issuperset(other)
s.isdisjoint(other)

# OPERATIONS
s1 | s2          # Union
s1 & s2          # Intersection
s1 - s2          # Difference
s1 ^ s2          # Symmetric difference

# ITERATE
for x in s:
for x in sorted(s):

# COPY
new = s.copy()
new = set(s)

# CONVERT
list(s)
tuple(s)
sorted(s)
```

---

## Key Takeaways

✅ Sets store **unique** elements only
✅ Sets are **unordered** - no indexing
✅ **Fast membership testing** - O(1) vs O(n) for lists
✅ Perfect for **removing duplicates**
✅ Powerful **set operations**: union, intersection, difference
✅ Elements must be **immutable** (hashable)
✅ Use `set()` not `{}` for empty sets
✅ Great for **mathematical operations** on collections

**Next Steps:** Practice with real problems! Try finding common friends between users, deduplicating data, or implementing tag systems.
