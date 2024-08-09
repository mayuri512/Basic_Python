#String
# Certainly! Here's a concise note on strings in Python:

# Definition: A string in Python is a sequence of characters enclosed within either single quotes (') or double quotes ("). For example: "Hello, World!" or 'Python'.

# Immutable: Strings are immutable, meaning their contents cannot be changed after creation. However, you can create new strings based on existing ones.

# Indexing and Slicing: You can access individual characters of a string using indexing, where the first character has index 0. Slicing allows you to extract substrings by specifying start, stop, and step values.

# Concatenation: Strings can be concatenated using the + operator, or by using the += operator for in-place concatenation.

# String Methods: Python provides a variety of built-in methods to manipulate strings, such as split(), join(), strip(), replace(), upper(), lower(), capitalize(), find(), count(), startswith(), endswith(), and many more.

# Formatted Strings: Python supports formatted string literals (f-strings) for easy string interpolation. For example: name = "Alice"; age = 30; f"My name is {name} and I'm {age} years old".

# Escape Characters: Strings can contain special escape characters like \n for newline, \t for tab, \" for double quote, and \' for single quote.

# Unicode Support: Python 3 uses Unicode by default, allowing strings to represent characters from various languages and symbols from different writing systems.

# Triple Quotes: Triple quotes (''' or """) can be used to create multi-line strings or to include special characters without escaping.

# Raw Strings: Raw strings (r"" or r'') treat backslashes as literal characters, useful for specifying regular expressions and file paths.

# String Operations: Python supports various string operations like checking membership with in, comparing with other strings using comparison operators, finding the length using len(), and iterating over characters with loops.

# Strings are fundamental data types in Python, extensively used for text processing, data manipulation, and communication with users.

a = "Ram is a good boy!"
print(a)

#Slicer
x = "Hello world!"

print(x[7])

# Normal slicer
print(x[3:5])
