"""
Example 19 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Basic Tryexcept
"""

# BASIC TRY/EXCEPT

try:
    risky_code()
except SpecificError:
    handle_error()

# MULTIPLE EXCEPTIONS

try:
    risky_code()
except ValueError:
    handle_value_error()
except KeyError:
    handle_key_error()
except Exception as e:
    print(f"Unexpected: {e}")

# WITH ELSE AND FINALLY

try:
    risky_code()
except Error:
    handle_error()
else:
    # Runs if no exception
    success_code()
finally:
    # Always runs
    cleanup()

# RAISE EXCEPTIONS

if invalid:
    raise ValueError("Invalid value")

# CUSTOM EXCEPTIONS

class CustomError(Exception):
    pass

raise CustomError("Something wrong")

# COMMON PATTERNS

# Safe conversion
try:
    num = int(user_input)
except ValueError:
    num = 0

# Safe file operation
try:
    with open("file.txt") as f:
        data = f.read()
except FileNotFoundError:
    data = ""

# Safe dictionary access
try:
    value = my_dict[key]
except KeyError:
    value = default
