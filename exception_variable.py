"""
reassignment does not happen on exception
"""

test_var = "original value"

try:
    test_var = test_var + 1
except Exception:
    pass

print(test_var)