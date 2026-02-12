# 📚 Python Dictionary Crash Course
*Master Python's Most Powerful Data Structure*

---

## 1. The Basics

Dictionaries are Python’s hash tables — key-value pairs designed for fast lookups.

### Creating Dictionaries

```python
# Empty dictionary
empty = {}
empty = dict()

# With initial values
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'NYC'
}

# Using dict() constructor
person = dict(name='Alice', age=30, city='NYC')

# From two lists
keys = ['name', 'age', 'city']
values = ['Bob', 25, 'LA']
person = dict(zip(keys, values))

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
```

> 💡 **Key Rule:** Keys must be immutable (strings, numbers, tuples). Values can be anything.

---

## 2. Accessing Values

### Using `[ ]` Brackets

```python
person = {'name': 'Alice', 'age': 30}

name = person['name']
city = person['city']  # ❌ KeyError
```

### Using `.get()`

```python
person = {'name': 'Alice', 'age': 30}

name = person.get('name')
city = person.get('city')
city = person.get('city', 'Unknown')
```

> ✅ **Best Practice:** Use `.get()` when a key might not exist.

---

## 3. Adding & Modifying

```python
person = {'name': 'Alice'}

person['age'] = 30
person['city'] = 'NYC'

person['age'] = 31

person.setdefault('country', 'USA')

person.update({'job': 'Engineer', 'salary': 100000})
person.update(job='Engineer', salary=100000)

defaults = {'theme': 'dark', 'lang': 'en'}
settings = {'lang': 'es', 'size': 'large'}
merged = defaults | settings
```

---

## 4. Removing Items

```python
person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}

del person['city']

age = person.pop('age')
job = person.pop('job', None)

item = person.popitem()

person.clear()
```

---

## 5. Iterating Through Dictionaries

```python
person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}

for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")
```

> 💡 Since Python 3.7+, dictionaries preserve insertion order.

---

## 6. Checking Membership

```python
person = {'name': 'Alice', 'age': 30}

if 'name' in person:
    print("Exists")

if 'city' not in person:
    print("Missing")

if 'Alice' in person.values():
    print("Alice found")

age = person.get('age')
```

---

## 7. Essential Methods Cheat Sheet

| Method | Purpose | Example |
|--------|----------|----------|
| `.get()` | Safe access | `d.get('x', 0)` |
| `.setdefault()` | Get or set | `d.setdefault('count', 0)` |
| `.update()` | Merge dict | `d.update({'x': 1})` |
| `.pop()` | Remove & return | `d.pop('x', None)` |
| `.popitem()` | Remove last | `k, v = d.popitem()` |
| `.keys()` | View keys | `for k in d.keys()` |
| `.values()` | View values | `for v in d.values()` |
| `.items()` | View pairs | `for k, v in d.items()` |
| `.clear()` | Remove all | `d.clear()` |
| `.copy()` | Shallow copy | `new = d.copy()` |

---

## 8. Common Patterns

### Counting

```python
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
```

Better:

```python
from collections import Counter
word_count = Counter(words)
```

---

### Filtering

```python
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
passing = {k: v for k, v in scores.items() if v >= 80}
```

---

## 9. Dictionary Comprehensions

```python
squares = {x: x**2 for x in range(6)}

evens = {x: x**2 for x in range(10) if x % 2 == 0}

upper_keys = {k.upper(): v for k, v in squares.items()}
```

---

## 10. Nested Dictionaries

```python
users = {
    'alice': {'age': 30},
    'bob': {'age': 25}
}

alice_age = users['alice']['age']
bob_phone = users.get('bob', {}).get('phone', 'N/A')
```

---

## 11. Practice Challenges

```python
sentence = "the quick brown fox jumps over the lazy dog"

phonebook = {}

scores = {
    'Al
