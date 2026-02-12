# Variables and DataTypes
# Python variables are created when you assign a value — no need to declare types.
name="Rishu"
num = 10
height= 56.3
is_developer=True

print(f"the variable if of type {type(name)}")
print(f"the variable if of type {type(num)}")
print(f"the variable if of type {type(height)}")
print(f"the variable if of type {type(is_developer)}")
print(f"length of string is {len(name)}")


# Strings
# Strings can be single quotes, double quotes, or triple quotes.
# Java: Strings are immutable — once created, they cannot be changed.
# Python: Strings are also immutable. Any operation like .upper() or concatenation creates a new string.

# Common operations
text="Python"
print(f"text in lowercaae {text.lower()}")
print(f"text in uppercase {text.upper()}")
print(f"extract character {text[0]}")
print(f"extract last character {text[-1]}")
print(f"extract second last character {text[-2]}")
print(f"extract characters {text[0:3]}")

# String immutability
# Strings in Python are immutable. This means that once we assign a value to a string, we can’t update it later. How about verifying it with an executable below?
str1 = "Hello"
print(str1)
str1 = "World"
print(str1)
# Running the above doesn't give an error. Does that contradict the rule that Python strings are immutable?
# No, it does not. What is happening under the hood in this case is that Python automatically creates
# a new space in memory for the new string using the same variable name. The older variable and the
# corresponding memory space remain unchanged and are eventually cleaned up and reclaimed by the system.


# String Comparison Tutorial in Python
print("String Comparison Tutorial in Python")
print("="*40)
print("1. Equality and Inequality")
print("="*40)

s1 = "hello"
s2 = "hello"
s3 = "world"

print(f"{s1} == {s2} ->", s1 == s2)   # True
print(f"{s1} != {s3} ->", s1 != s3)   # True
print(f"{s1} == {s3} ->", s1 == s3)   # False

print("\n" + "="*40)
print("2. Lexicographical (Alphabetical) Comparison")
print("="*40)

print('"apple" < "banana" ->', "apple" < "banana")  # True
print('"apple" > "Banana" ->', "apple" > "Banana")  # True (lowercase > uppercase)
print('"Zoo" < "apple" ->', "Zoo" < "apple")        # True (uppercase comes first)

print("\n" + "="*40)
print("3. Case-Insensitive Comparison")
print("="*40)

s4 = "Python"
s5 = "python"

print(f"{s4}.lower() == {s5}.lower() ->", s4.lower() == s5.lower())   # True
print(f"{s4}.casefold() == {s5}.casefold() ->", s4.casefold() == s5.casefold()) # True

print("\n" + "="*40)
print("4. Substring Checks")
print("="*40)

s6 = "python programming"

print('"py" in s6 ->', "py" in s6)           # True
print('"java" in s6 ->', "java" in s6)       # False
print('"program" in s6 ->', "program" in s6) # True
print('"py" not in s6 ->', "py" not in s6)   # False

print("\n" + "="*40)
print("5. startswith() and endswith()")
print("="*40)

s7 = "programming"

print('s7.startswith("pro") ->', s7.startswith("pro"))  # True
print('s7.endswith("ing") ->', s7.endswith("ing"))      # True
print('s7.endswith("xyz") ->', s7.endswith("xyz"))      # False

print("\n" + "="*40)
print("6. Comparing with special characters")
print("="*40)

print('"ß".lower() == "ss" ->', "ß".lower() == "ss")       # False
print('"ß".casefold() == "ss" ->', "ß".casefold() == "ss") # True (casefold handles ß properly)


print("="*40)
print("How do you split and join strings in Python?")
print("="*40)

text = "apple,banana,cherry"

# Split on comma
fruits = text.split(",")
print(fruits)
# ['apple', 'banana', 'cherry']

# Split on whitespace (default)
sentence = "Python is fun"
words = sentence.split()
print(words)
# ['Python', 'is', 'fun']

# Split only on the first occurrence
limited = text.split(",", 1)
print(limited)
# ['apple', 'banana,cherry']

# The join() method does the reverse — it combines a list of strings into a single string with a separator.
fruits_str = "--".join(fruits)
print(fruits_str)

# How to reverse a string
text = "Python again"
print(f"Reverse of string is {text[::-1]}")

