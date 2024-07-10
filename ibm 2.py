# Creating a sample list
my_list = [1, 2, 3, 4, 5]

# Display the original list
print(f"Original List: {my_list}")

# 1. append(): Add an element to the end of the list
my_list.append(6)
print(f"1. append(6): {my_list}")

# 2. extend(): Extend the list by appending elements from an iterable
my_list.extend([7, 8, 9])
print(f"2. extend([7, 8, 9]): {my_list}")

# 3. insert(): Insert an element at a specified position
my_list.insert(1, 10)
print(f"3. insert(1, 10): {my_list}")

# 4. remove(): Remove the first occurrence of a specified value
my_list.remove(3)
print(f"4. remove(3): {my_list}")

# 5. pop(): Remove and return the element at a specified position (default is the last element)
popped_element = my_list.pop(2)
print(f"5. pop(2): {my_list}, Popped Element: {popped_element}")

# 6. index(): Return the index of the first occurrence of a specified value
index_of_5 = my_list.index(5)
print(f"6. index(5): {index_of_5}")

# 7. count(): Count the number of occurrences of a specified value
count_of_5 = my_list.count(5)
print(f"7. count(5): {count_of_5}")

# 8. sort(): Sort the list in ascending order (modifies the original list)
my_list.sort()
print(f"8. sort(): {my_list}")

# 9. reverse(): Reverse the elements of the list in-place
my_list.reverse()
print(f"9. reverse(): {my_list}")

# 10. copy(): Create a shallow copy of the list
copied_list = my_list.copy()
print(f"10. copy(): {copied_list}")

# 11. clear(): Remove all elements from the list
my_list.clear()
print(f"11. clear(): {my_list}")
