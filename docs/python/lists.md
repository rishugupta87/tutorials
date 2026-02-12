# 📋 Python Lists Crash Course

Master Python's most versatile data structure

---

## 1. The Basics

Lists are ordered, mutable collections that can hold any type of data.

### Creating Lists

```python
# Empty list
empty = []
empty = list()

# With initial values
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]

# Using list() constructor
chars = list("hello")  # ['h', 'e', 'l', 'l', 'o']

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using range
numbers = list(range(5))  # [0, 1, 2, 3, 4]
evens = list(range(0, 10, 2))  # [0, 2, 4, 6, 8]
```

**💡 Tip:** Lists can contain different data types, even other lists!

---

## 2. Accessing Elements

### Indexing (0-based)

```python
fruits = ['apple', 'banana', 'cherry', 'date']

# Access by index
first = fruits[0]      # 'apple'
second = fruits[1]     # 'banana'

# Negative indexing (from end)
last = fruits[-1]      # 'date'
second_last = fruits[-2]  # 'cherry'

# IndexError if out of range
# fruits[10]  # ❌ IndexError!
```

### Slicing [start:stop:step]

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
numbers[2:5]    # [2, 3, 4] (stop is exclusive)
numbers[:3]     # [0, 1, 2] (start from beginning)
numbers[5:]     # [5, 6, 7, 8, 9] (go to end)
numbers[:]      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (copy entire list)

# With step
numbers[::2]    # [0, 2, 4, 6, 8] (every 2nd element)
numbers[1::2]   # [1, 3, 5, 7, 9] (odd numbers)
numbers[::-1]   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse!)

# Negative indices in slicing
numbers[-3:]    # [7, 8, 9] (last 3 elements)
numbers[:-2]    # [0, 1, 2, 3, 4, 5, 6, 7] (all except last 2)
```

**✅ Pro Tip:** `list[::-1]` is a quick way to reverse a list!

---

## 3. Modifying Lists

Lists are **mutable** - you can change them after creation.

### Adding Elements

```python
fruits = ['apple', 'banana']

# append() - add to end
fruits.append('cherry')
# ['apple', 'banana', 'cherry']

# insert() - add at specific position
fruits.insert(1, 'blueberry')
# ['apple', 'blueberry', 'banana', 'cherry']

# extend() - add multiple items
fruits.extend(['date', 'elderberry'])
# ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

# + operator - concatenate
more_fruits = fruits + ['fig', 'grape']

# * operator - repeat
zeros = [0] * 5  # [0, 0, 0, 0, 0]
```

### Removing Elements

```python
fruits = ['apple', 'banana', 'cherry', 'banana']

# remove() - remove first occurrence
fruits.remove('banana')
# ['apple', 'cherry', 'banana']

# pop() - remove by index and return it
last = fruits.pop()     # returns 'banana'
first = fruits.pop(0)   # returns 'apple'

# del - delete by index or slice
del fruits[0]           # delete first item
del fruits[1:3]         # delete slice

# clear() - remove all items
fruits.clear()  # []
```

### Modifying Elements

```python
numbers = [1, 2, 3, 4, 5]

# Change single element
numbers[0] = 10
# [10, 2, 3, 4, 5]

# Change slice
numbers[1:3] = [20, 30]
# [10, 20, 30, 4, 5]

# Replace with different length
numbers[2:4] = [100, 200, 300]
# [10, 20, 100, 200, 300, 5]
```

---

## 4. List Methods Cheat Sheet

| Method | What It Does | Example |
|--------|-------------|---------|
| `.append(x)` | Add x to end | `lst.append(5)` |
| `.extend(iterable)` | Add all items | `lst.extend([1,2,3])` |
| `.insert(i, x)` | Insert x at index i | `lst.insert(0, 'first')` |
| `.remove(x)` | Remove first x | `lst.remove('apple')` |
| `.pop(i)` | Remove & return item at i | `item = lst.pop()` |
| `.clear()` | Remove all items | `lst.clear()` |
| `.index(x)` | Find index of first x | `i = lst.index('banana')` |
| `.count(x)` | Count occurrences of x | `n = lst.count(5)` |
| `.sort()` | Sort in place | `lst.sort()` |
| `.reverse()` | Reverse in place | `lst.reverse()` |
| `.copy()` | Shallow copy | `new = lst.copy()` |

---

## 5. Sorting

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - modifies original list
numbers.sort()
# [1, 1, 2, 3, 4, 5, 6, 9]

# sort descending
numbers.sort(reverse=True)
# [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() - returns new sorted list
original = [3, 1, 4, 1, 5]
new_list = sorted(original)
# original: [3, 1, 4, 1, 5]
# new_list: [1, 1, 3, 4, 5]

# Sort with key function
words = ['apple', 'pie', 'banana', 'a']
words.sort(key=len)  # Sort by length
# ['a', 'pie', 'apple', 'banana']

# Sort complex objects
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]
students.sort(key=lambda x: x['grade'], reverse=True)
# Sorted by grade, highest first
```

---

## 6. Checking & Searching

```python
fruits = ['apple', 'banana', 'cherry']

# Check if item exists
if 'apple' in fruits:
    print("Found!")

if 'grape' not in fruits:
    print("Not found!")

# Find index
index = fruits.index('banana')  # 1
# fruits.index('grape')  # ❌ ValueError if not found!

# Count occurrences
numbers = [1, 2, 2, 3, 2, 4]
count = numbers.count(2)  # 3

# Length
length = len(fruits)  # 3

# Min/Max (for comparable items)
numbers = [3, 1, 4, 1, 5]
smallest = min(numbers)  # 1
largest = max(numbers)   # 5
total = sum(numbers)     # 14
```

---

## 7. List Comprehensions

Powerful one-liner to create lists.

### Basic Syntax

```python
# Syntax: [expression for item in iterable]

# Squares
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

# Uppercase words
words = ['hello', 'world']
upper = [word.upper() for word in words]
# ['HELLO', 'WORLD']

# Extract from complex data
users = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
names = [user['name'] for user in users]
# ['Alice', 'Bob']
```

### With Conditions (Filtering)

```python
# Syntax: [expression for item in iterable if condition]

# Even numbers only
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
# [2, 4, 6, 8, 10]

# Positive numbers only
mixed = [-2, -1, 0, 1, 2, 3]
positive = [x for x in mixed if x > 0]
# [1, 2, 3]

# Filter and transform
words = ['apple', 'pie', 'banana', 'a']
long_words = [w.upper() for w in words if len(w) > 3]
# ['APPLE', 'BANANA']
```

### Conditional Expressions

```python
# Syntax: [expression_if_true if condition else expression_if_false for item in iterable]

# Mark even/odd
numbers = [1, 2, 3, 4, 5]
labels = ['even' if x % 2 == 0 else 'odd' for x in numbers]
# ['odd', 'even', 'odd', 'even', 'odd']

# Cap values
values = [1, 5, 10, 15, 20]
capped = [x if x <= 10 else 10 for x in values]
# [1, 5, 10, 10, 10]
```

### Nested Comprehensions

```python
# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create 2D list
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

**💡 When to Use:** Great for simple transformations. If logic gets complex, use a regular loop!

---

## 8. Iterating Through Lists

```python
fruits = ['apple', 'banana', 'cherry']

# Basic iteration
for fruit in fruits:
    print(fruit)

# With index using enumerate()
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Start from different index
for i, fruit in enumerate(fruits, start=1):
    print(f"#{i}: {fruit}")
# #1: apple
# #2: banana
# #3: cherry

# Iterate two lists together with zip()
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Iterate in reverse
for fruit in reversed(fruits):
    print(fruit)
```

---

## 9. Copying Lists

```python
original = [1, 2, 3]

# ❌ WRONG - This creates a reference!
copy1 = original
copy1.append(4)
# Both original and copy1 are now [1, 2, 3, 4]

# ✅ CORRECT Ways to Copy

# Method 1: slice
copy2 = original[:]

# Method 2: .copy()
copy3 = original.copy()

# Method 3: list()
copy4 = list(original)

# Method 4: copy module (for nested lists)
import copy
nested = [[1, 2], [3, 4]]
shallow = nested.copy()  # Outer list copied, inner lists referenced
deep = copy.deepcopy(nested)  # Everything copied
```

**⚠️ Warning:** Simple copy methods are SHALLOW - nested lists are still referenced!

---

## 10. Common Patterns

### Remove Duplicates (Keep Order)

```python
# Method 1: Loop (preserves order)
items = [1, 2, 2, 3, 1, 4, 3]
unique = []
for item in items:
    if item not in unique:
        unique.append(item)
# [1, 2, 3, 4]

# Method 2: dict.fromkeys() (Python 3.7+)
unique = list(dict.fromkeys(items))
# [1, 2, 3, 4]

# Method 3: set (doesn't preserve order)
unique = list(set(items))
# [1, 2, 3, 4] (order not guaranteed)
```

### Flatten Nested List

```python
nested = [[1, 2], [3, 4], [5]]

# Using list comprehension
flat = [item for sublist in nested for item in sublist]
# [1, 2, 3, 4, 5]

# Using extend
flat = []
for sublist in nested:
    flat.extend(sublist)
```

### Filter Out None/Empty Values

```python
items = [1, None, 2, '', 3, 0, False, 4]

# Remove all falsy values
filtered = [x for x in items if x]
# [1, 2, 3, 4]

# Remove only None
filtered = [x for x in items if x is not None]
# [1, 2, '', 3, 0, False, 4]
```

### Split List into Chunks

```python
items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3

chunks = [items[i:i+chunk_size] for i in range(0, len(items), chunk_size)]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Find Common Elements

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Using set intersection
common = list(set(list1) & set(list2))
# [4, 5]

# Using list comprehension
common = [x for x in list1 if x in list2]
# [4, 5]
```

---

## 11. List vs Tuple vs Set

| Feature | List | Tuple | Set |
|---------|------|-------|-----|
| Mutable | ✅ Yes | ❌ No | ✅ Yes |
| Ordered | ✅ Yes | ✅ Yes | ❌ No |
| Duplicates | ✅ Yes | ✅ Yes | ❌ No |
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` |
| Use Case | General purpose | Immutable data | Unique items |

---

## 12. Common Mistakes

### ❌ Modifying List While Iterating

```python
# WRONG
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Skips elements!

# CORRECT
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
```

### ❌ Multiplying Lists with Mutable Objects

```python
# WRONG - Creates references to same list!
matrix = [[0] * 3] * 3
matrix[0][0] = 1
# [[1, 0, 0], [1, 0, 0], [1, 0, 0]]  # All rows changed!

# CORRECT
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 1
# [[1, 0, 0], [0, 0, 0], [0, 0, 0]]  # Only first row changed
```

### ❌ Using + in Loops

```python
# SLOW - Creates new list each time
result = []
for i in range(1000):
    result = result + [i]  # O(n) each iteration!

# FAST - Modifies in place
result = []
for i in range(1000):
    result.append(i)  # O(1) each iteration
```

---

## 13. Quick Reference

```python
# CREATE
lst = []
lst = [1, 2, 3]
lst = list(range(5))
lst = [x for x in range(5)]

# ACCESS
lst[0]        # First
lst[-1]       # Last
lst[1:3]      # Slice
len(lst)      # Length

# MODIFY
lst.append(x)
lst.extend([1, 2])
lst.insert(i, x)
lst[i] = x
del lst[i]
lst.remove(x)
lst.pop()
lst.clear()

# SEARCH
x in lst
x not in lst
lst.index(x)
lst.count(x)

# SORT
lst.sort()
lst.reverse()
sorted(lst)
reversed(lst)

# COPY
new = lst[:]
new = lst.copy()
new = list(lst)

# ITERATE
for x in lst:
for i, x in enumerate(lst):
for x, y in zip(lst1, lst2):
```

---

## Key Takeaways

✅ Lists are mutable and ordered
✅ Use slicing `[start:stop:step]` for powerful access
✅ List comprehensions for concise transformations
✅ `.append()` for single items, `.extend()` for multiple
✅ Use `enumerate()` when you need both index and value
✅ `lst[:]` creates a copy, `lst2 = lst` creates a reference
✅ Don't modify lists while iterating - use comprehensions instead

**Next Steps:** Practice with real problems! Try building a to-do list manager or data filter.
