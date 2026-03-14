"""
Example 9 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Example 09
"""

try:
    # Code that might raise exception
    result = risky_operation()

except SpecificError:
    # Handle specific error
    handle_specific_error()

except AnotherError as e:
    # Handle another error
    print(f"Error: {e}")

except Exception as e:
    # Catch any other exception
    print(f"Unexpected error: {e}")

else:
    # Runs only if no exception
    print("Success!")

finally:
    # Always runs
    cleanup()
