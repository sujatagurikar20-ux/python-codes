fruits_tuple = ("apple", "banana", "cherry", "apple", "elderberry")
print("Original Tuple:", fruits_tuple)

print("First element:", fruits_tuple[0])
print("Last element:", fruits_tuple[-1])
print("Sliced elements (1 to 3):", fruits_tuple[1:4])

if "banana" in fruits_tuple:
    print("'banana' is present in the tuple.")

print("Length of the tuple:", len(fruits_tuple))
print("Count of 'apple':", fruits_tuple.count("apple"))

print("Index of 'cherry':", fruits_tuple.index("cherry"))

more_fruits = ("fig", "grape")
combined_tuple = fruits_tuple + more_fruits
print("Concatenated Tuple:", combined_tuple)

repeated_tuple = more_fruits * 2
print("Repeated Tuple:", repeated_tuple)
