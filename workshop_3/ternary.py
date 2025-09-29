"""
status should "Hot" after 35 degrees and "Not Hot" under it
"""
temp = 29

# if temp > 30:
#     status = "Hot"
# else:
#     # indentation
#     status = "Not Hot"

# ternary operator
status = "Hot" if temp > 30 else "Not Hot"

print(f"Status: {status}") # Not Hot