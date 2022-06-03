import re

LIMITS = (1, 100)

line = input("Enter integers between %d and %d: " % LIMITS)

# parse input for all possible numbers
numbers = [int(digits) for digits in re.findall(r'[0-9]+', line)]

# filter for valid numbers in given range
numbers = [n for n in numbers if LIMITS[0] <= n <= LIMITS[1]]

# count occurences; save in dict for easy use later
occurences = {}
for number in numbers:
    if number in occurences:
        occurences[number] += 1
    else:
        occurences[number] = 1

print(occurences)
