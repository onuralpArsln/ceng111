import re

# List of keywords
keywords = ["help", "twosum", "sumodd"]

# User input
user_input = "smTwo"

# Normalize user input to lowercase
normalized_input = user_input.lower()

# Define a regular expression pattern that matches each keyword with optional additional characters
pattern = "(" + "|".join(keywords) + r")\w*"

# Create a regex object with the pattern and specify case-insensitive matching
regex = re.compile(pattern, re.IGNORECASE)

# Use search method to find a match
match = regex.search(normalized_input)

# Check if a match is found
if match:
    # Get the matched keyword
    matched_keyword = match.group()
    print("Detected keyword:", matched_keyword)
else:
    print("No keyword detected.")

print("Pattern:", pattern)
print("Normalized input:", normalized_input)


