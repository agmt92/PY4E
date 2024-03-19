fhand = open('text-file.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) <= 3 or words[0] != 'From' : continue
    # if words[0] != 'From' : continue
    #print('debug1', len(words))
    #print('Debug:', words)
    print(words[2])
