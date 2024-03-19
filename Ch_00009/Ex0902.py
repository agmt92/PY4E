fhand = open ('mbox-short.txt')
count = 0
many = dict()
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) <= 3 or words[0] != 'From' : continue
    # if words[0] != 'From' : continue
    #print('Debug:', words)
    z=words[2]
    count = count + 1
    #print(z)
    many[z] = many.get(z, 0) + 1

print(many)



# print('There were', count,'lines in the file with From as the first word')
