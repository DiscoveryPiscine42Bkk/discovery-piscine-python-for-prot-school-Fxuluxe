original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = list(set(num + 2 for num in original_array if num > 5))

print("Original array:", original_array)
print("New array:", new_array)
