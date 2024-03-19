fhand = open ('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) <= 3 or words[0] != 'From' : continue
    # if words[0] != 'From' : continue
    #print('Debug:', words)
    z = len(words)
    print(words[1])
    count = count + 1

print('There were', count,'lines in the file with From as the first word')
