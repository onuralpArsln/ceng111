print(ord('A'))  # Output: 65
print(ord('a'))  # Output: 97
print(ord('1'))  # Output: 49



def simple_hash(string):
    """
    A simple hash function that calculates the hash value
    of a string by summing up the ASCII values of its characters.
    """
    hash_value = 0
    for char in string:
        hash_value += ord(char)  #it returns an integer representing the Unicode code of the character passed to it.
    return hash_value

# Example usage
input_string = "hello"
hash_value = simple_hash(input_string)
print("Hash value of '{}': {}".format(input_string, hash_value))