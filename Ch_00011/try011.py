import re
count = 0
hand = open('mbox-short.txt')
serinput = input('Enter a regular expression: ')

for line in hand:
    line = line.rstrip()
    if re.search(serinput ,line):
        count = count + 1
    if serinput == 'done':
        print('Exiting.....')
if serinput != 'done':
    print('mbox-short.txt','had', count, 'lines that matched ', serinput)
