# main.py
from testpypi import mymodule

# Accessing the function using dot notation
message = mymodule.greeting("Jonathan")
print(message)  # Output: Hello, Jonathan!

# Accessing the variable
print(mymodule.person["name"])  # Output: Alice
