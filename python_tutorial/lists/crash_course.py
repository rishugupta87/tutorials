######## variable types supported ######
a = 5
b = 10.2
c = "ring"
d = True
print(f"a {a}, b {b}, c {c}, d {d}")

############################### ############################### lists in python ##############################################################
nums = [1, 2, 3, 4, 5, 0, -3, -5]

print("nums:", nums)
print("unpacked:", *nums)

# Membership test
is_element = 2 in nums
print(f"element present? {is_element}")

# Show mixed types allowed
nums.append("lion")
nums.append(89)
print("after append (mixed types):", nums)

# Pop
popped = nums.pop()
print("popped:", popped)
print("after pop:", nums)

# Reverse in-place
nums.reverse()
print("reversed:", nums)

# Remove string before sorting
nums.remove("lion")
print("after removing lion:", nums)

# Sort numeric list
nums.sort()
print("sorted:", nums)

# Slicing
print("first 5 elements:", nums[:5])

nums2 = nums[1:6:2]
print("nums2 (slice 1:6:2):", nums2)

# Insert
nums.insert(2, 11)
print("after insert nums:", nums)

# Concatenation
nums3 = nums + nums2
print("nums3:", nums3)

# Reverse copy (slice)
print("nums3 reversed copy:", nums3[::-1])
print("nums3 original still same:", nums3)

# Reverse in-place
nums3.reverse()
print("nums3 reversed in place:", nums3)

# Nested list
complex_lists = [nums, nums2, ["apple", "banana"]]
print("complex_lists:", complex_lists)

# iterating over the lists
for num in nums:
    print("num:", num)
for i in range(len(nums)):
    print("num using range:", nums[i])
for i, num in enumerate(nums):
    print("using enumerate:", i, num)

# using list comprehension -> Create a new list by applying an expression to each element.
# new_list = [expression for item in iterable]
# List comprehension is for creating new lists. if you are just printing numbers dont use list comprehension as it wasters memory
copy_nums = [num for num in nums] # copy the list to another
print("copy_nums:", copy_nums)
print("check if even", [num%2==0 for num in nums])
print("evens only", [num for num in nums if num % 2 == 0])
print("conditional expression", ["even" if num % 2 == 0 else "odd" for num in nums])

# conditional expression
