# Get user input
user_input = input('enter integers: ')

# Convert input to a list
number_list = user_input.split()

# Initialize empty list
result_list = []

# Check if value has negative integer
for item in number_list:
    num = int(item)

    if num < 0:
        continue

    result_list.append(num)

# Sort the list of non-negative integers
result_list.sort()

# Convert the sorted list to a string with spaces between elements
result_string = ' '.join(map(str, result_list))

print(result_string, end=' ')
