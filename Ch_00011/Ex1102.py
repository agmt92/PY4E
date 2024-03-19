# Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.
import re
tot = int()

hand = open('regex_sum_1984815.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    for nums in x:
        z = int(nums)
        tot = tot + z
print(tot)
