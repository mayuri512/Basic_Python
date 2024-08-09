# Slicing in Python refers to extracting a portion of a sequence (such as a list, tuple, or string) using a specified range. Here are the key points about slicing:

# Syntax: The general syntax for slicing is sequence[start:stop:step], where:

# start: Optional. The starting index of the slice (inclusive). If omitted, slicing starts from the beginning of the sequence.
# stop: Required. The ending index of the slice (exclusive). Slicing stops before this index.
# step: Optional. The step or increment by which to move through the sequence. If omitted, the default value is 1.
# Indexing: Slicing uses zero-based indexing, meaning the first element has index 0, the second has index 1, and so on.

# Negative Indices: Negative indices can be used to specify positions relative to the end of the sequence. -1 refers to the last element, -2 refers to the second to last, and so forth.

# Default Values: If start is omitted, slicing starts from the beginning of the sequence. If stop is omitted, slicing goes to the end of the sequence. If step is omitted, the default value is 1.

# Extracting Subsequences: Slicing allows you to extract a portion of a sequence, creating a new sequence with the selected elements.

# Modifying Sequences: Slicing can also be used to modify elements within a sequence by assigning new values to the sliced portion.

# Common Idioms:

# sequence[:]: Creates a shallow copy of the entire sequence.
# sequence[start:]: Creates a slice from start to the end of the sequence.
# sequence[:stop]: Creates a slice from the beginning of the sequence to stop-1.
# sequence[::step]: Creates a slice with a step size of step.
# sequence[::-1]: Reverses the sequence.
# Immutable Sequences: Slicing immutable sequences like strings and tuples returns new sequences because these types are immutable.

# Mutable Sequences: Slicing mutable sequences like lists allows for modification of the original sequence because lists are mutable.

# Slicing is a powerful feature in Python that provides a concise and efficient way to work with subsequences of data.
#Slicing 
x = "Hello world"
print(x[0:4])
print(x[-4:-2])
print(x[-6:-3])

#pattern Slicing
print(x[-3:-9:-1])

y = x.lower()
print(y)
