#if else statement 

# If Statement: The if statement is used to execute a block of code only if a specified condition is true. It has the following syntax:

# if condition:
#     # Code block to be executed if condition is true
# If-else Statement: The if-else statement allows you to execute one block of code if the condition is true and another block if the condition is false. It has the following syntax:

# if condition:
#     # Code block to be executed if condition is true
# else:
#     # Code block to be executed if condition is false
# If-elif-else Statement: The if-elif-else statement allows you to check multiple conditions and execute different blocks of code based on which condition is true. It has the following syntax:

# if condition1:
#     # Code block to be executed if condition1 is true
# elif condition2:
#     # Code block to be executed if condition1 is false and condition2 is true
# else:
#     # Code block to be executed if all conditions are false
# Nested Conditional Statements: Conditional statements can be nested within each other to handle more complex scenarios. For example:

# if condition1:
#     if condition2:
#         # Code block to be executed if both condition1 and condition2 are true
#     else:
#         # Code block to be executed if condition1 is true and condition2 is false
# else:
#     # Code block to be executed if condition1 is false
# Ternary Operator: Python supports a shorthand syntax for simple if-else statements, called the ternary operator. It has the following syntax:


# x = value_if_true if condition else value_if_false
# This is equivalent to:

# if condition:
#     x = value_if_true
# else:
#     x = value_if_false
# Conditional statements are fundamental for controlling the flow of a program based on different conditions, allowing you to write more dynamic and responsive code.

age = int(input("Enter your age:"))

if age < 1 or age > 100:
    print("Invalid age.")
else:
    if age >= 19:
        print("Eligible")
    else:
        print("Not eligible")
        100