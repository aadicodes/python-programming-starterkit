"""
Example 13 from Chapter 9: Preserving Data - File Operations
Python Programming Fundamentals by Rajesh Aadi

Safe Read Json
"""

def safe_read_json(filename, default=None):
    """Safely read JSON file with error handling"""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found, using default")
        return default if default is not None else {}
    except json.JSONDecodeError:
        print(f"Invalid JSON in {filename}")
        return default if default is not None else {}

def safe_write_json(filename, data):
    """Safely write JSON file with error handling"""
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)
        return True
    except PermissionError:
        print(f"No permission to write {filename}")
        return False
    except Exception as e:
        print(f"Error writing file: {e}")
        return False

# Usage
data = safe_read_json("customers.json", {"customers": []})
data["customers"].append({"name": "Alice", "points": 100})
safe_write_json("customers.json", data)
