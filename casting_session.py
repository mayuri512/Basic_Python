#Castinga:
# Type casting in Python refers to the process of converting a variable from one data type to another. Here are some common methods of type casting in Python:

# Implicit Type Casting: Python automatically converts data types when needed, typically during arithmetic operations or comparisons between different types. For example, adding an integer to a floating-point number will result in a float.

# Explicit Type Casting: You can explicitly convert variables from one type to another using built-in functions. The most common ones are:

# int(): Converts a variable to an integer. If the variable is a floating-point number, it truncates the decimal part.

# float(): Converts a variable to a floating-point number.

# str(): Converts a variable to a string.

# bool(): Converts a variable to a boolean. Any non-zero value or non-empty object will be converted to True, while zero or None will be converted to False.

# list(), tuple(), set(): Convert a variable to a list, tuple, or set, respectively.

# dict(): Converts a variable to a dictionary.

# Type-specific Casting Functions: Certain data types have their own methods for type conversion. For instance:

# int() can also convert strings representing integers to integers, like int("123").

# float() can convert strings representing floating-point numbers to floats, like float("3.14").

# Custom Type Casting: You can define custom functions or methods to perform more complex type casting, especially for user-defined classes.

# It's important to handle type casting carefully, especially when converting between different data types, as data loss or unexpected behavior may occur if the conversion is not done properly.

x = 100
z = 0
print(x)

y = float(x)
print(y)
print(type(y))

a = complex(x)
print(a)
print(type(a))

b = str(x)
print(b)
print(type(b))

c = bool(x)
print(c)
print(type(c))

d = bool(z)
print(d)
print(type(d))
