# Define a sample string
sample_string = "helloFun"

# capitalize(): Capitalize the first character of the string
capitalized_string = sample_string.capitalize()
print(f"capitalize(): {capitalized_string}")

# count(): Count occurrences of a substring in the string
substring_count = sample_string.count("o")
print(f"count('o'): {substring_count}")

# endswith(): Check if the string ends with a specified suffix
suffix_check = sample_string.endswith("Fun.")
print(f"endswith('Fun.'): {suffix_check}")

# find(): Find the index of the first occurrence of a substring
substring_index = sample_string.find("World")
print(f"find('World'): {substring_index}")

# index(): Like find(), but raises ValueError if the substring is not found
try:
    substring_index = sample_string.index("Python")
    print(f"index('Python'): {substring_index}")
except ValueError as e:
    print(f"index('Python'): {e}")

# isalpha(): Check if all characters are alphabetic
is_alpha_check = sample_string.isalpha()
print(f"isalpha(): {is_alpha_check}")

# isdecimal(): Check if all characters are decimals
is_decimal_check = sample_string.isdecimal()
print(f"isdecimal(): {is_decimal_check}")

# islower(): Check if all characters are in lowercase
is_lower_check = sample_string.islower()
print(f"islower(): {is_lower_check}")

# join(): Join elements of an iterable using the string as a separator
words = ["Python", "is", "awesome"]
joined_string = " ".join(words)
print(f"join(): {joined_string}")

# rjust(): Right justify the string in a field of specified width
right_justified_string = sample_string.rjust(30, "*")
print(f"rjust(30, '*'): {right_justified_string}")

# swapcase(): Swap the case of each character in the string
swapped_case_string = sample_string.swapcase()
print(f"swapcase(): {swapped_case_string}")

# strip(): Remove leading and trailing whitespaces or specified characters
stripped_string = sample_string.strip('!.')
print(f"strip('!.'): {stripped_string}")

# replace(): Replace occurrences of a substring with another substring
replaced_string = sample_string.replace("Python", "Java")
print(f"replace('Python', 'Java'): {replaced_string}")

# split(): Split the string into a list using a specified separator
split_list = sample_string.split(" ")
print(f"split(' '): {split_list}")

# len(): Get the length of the string
string_length = len(sample_string)
print(f"len(): {string_length}")

# ord(): Get the ASCII value of a character
ascii_value = ord('A')
print(f"ord('A'): {ascii_value}")

# ascii(): Get a string containing a printable representation of an object
ascii_representation = ascii(sample_string)
print(f"ascii(): {ascii_representation}")
