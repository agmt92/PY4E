import re

def search_file(serinput, hand):
    count = 0
    for line in hand:
        line = line.rstrip()
        if re.search(serinput, line):
            count += 1
    return count

hand = open('mbox-short.txt')

while True:
    serinput = input('Enter a regular expression: ')
    if serinput.lower() == "done":
        print("Exiting.....")
        break  # Use break to exit the loop, exit() is usually for terminating the program
    hand.seek(0)  # Reset file pointer to the beginning of the file
    count = search_file(serinput, hand)
    print('mbox-short.txt had', count, 'lines that matched', serinput)
