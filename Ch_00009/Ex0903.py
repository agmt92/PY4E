fhand = open ('mbox-short.txt')
many = dict()
for line in fhand:
    words = line.split()
    if len(words) <= 3 or words[0] != 'From' : continue
    z=words[1]
    many[z] = many.get(z, 0) + 1
print(many)
