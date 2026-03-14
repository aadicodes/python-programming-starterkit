"""
Example 14 from Chapter 11: Building Systems - Object-Oriented Programming
Python Programming Fundamentals by Rajesh Aadi

Class Definition
"""

# CLASS DEFINITION

class MyClass:
    # Class attribute
    class_var = "shared"

    def __init__(self, value):
        # Instance attribute
        self.value = value

    def method(self):
        # Instance method
        return self.value

# CREATE OBJECT

obj = MyClass("hello")
print(obj.value)
obj.method()

# INHERITANCE

class Child(Parent):
    def __init__(self, value):
        super().__init__()
        self.value = value

# PROPERTIES

class MyClass:
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

# SPECIAL METHODS

def __str__(self):
    return "string representation"

def __repr__(self):
    return "MyClass(value)"

def __eq__(self, other):
    return self.value == other.value

# PRIVATE ATTRIBUTES

class MyClass:
    def __init__(self):
        self.__private = "private"
        self._protected = "protected"
        self.public = "public"
