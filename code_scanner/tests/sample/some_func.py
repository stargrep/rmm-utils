# Function Programming
# Pure Function


def multiply_2_pure(numbers):
    new_numbers = []
    for n in numbers:
        new_numbers.append(n * 2)
    return new_numbers


original_numbers = [1, 3, 5, 10]
changed_numbers = multiply_2_pure(original_numbers)
print(original_numbers)  # [1, 3, 5, 10]
print(changed_numbers)  # [2, 6, 10, 20]


# Immutability
mutable_collection = ['Tim', 10, [4, 5]]
immutable_collection = ('Tim', 10, [4, 5])

# Reading from data types are essentially the same:
print(mutable_collection[2])    # [4, 5]
print(immutable_collection[2])  # [4, 5]


# Higher Order Functions
def hof_add(increment):
    # Create a function that loops and adds the increment
    def add_increment(numbers):
        new_numbers = []
        for n in numbers:
            new_numbers.append(n + increment)
        return new_numbers
    # We return the function as we do any other value
    return add_increment


add5 = hof_add(5)
print(add5([23, 88]))   # [28, 93]
add10 = hof_add(10)
print(add10([23, 88]))  # [33, 98]


# Lambda Expressions
def hof_product(multiplier):
    return lambda x: x * multiplier


m = hof_product(6)
print(m(6))  # 36


# Build-in Higher Order Functions
names = ['Shivani', 'Jason', 'Yusef', 'Sakura']
greeted_names = map(lambda x: 'Hi ' + x, names)

# This prints something similar to: <map object at 0x10ed93cc0>
print(greeted_names)
# Recall, that map returns an iterator

# We can print all names in a for loop
for name in greeted_names:
    print(name)

numbers = [13, 4, 18, 35]
div_by_5 = filter(lambda num: num % 5 == 0, numbers)

# We can convert the iterator into a list
print(list(div_by_5))  # [35]

# Let's arbitrarily get the all numbers divisible by 3 between 1 and 20 and cube them
arbitrary_numbers = map(lambda num: num ** 3, filter(lambda num: num % 3 == 0, range(1, 21)))

print(list(arbitrary_numbers)) # [27, 216, 729, 1728, 3375, 5832]

# List Comprehensions
# Recall
numbers = [13, 4, 18, 35]
# Instead of: filter(lambda num: num % 5 == 0, numbers), we can do
div_by_5 = [num for num in numbers if num % 5 == 0]

print(div_by_5)  # [35]

# We can manage the combined case as well:
# Instead of:
# map(lambda num: num ** 3, filter(lambda num: num % 3 == 0, range(1, 21)))
arbitrary_numbers = [num ** 3 for num in range(1, 21) if num % 3 == 0]
print(arbitrary_numbers)  # [27, 216, 729, 1728, 3375, 5832]

