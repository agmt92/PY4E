fhand = open ('mbox-short.txt')
many = dict()
for line in fhand:
    words = line.split()
    if len(words) <= 3 or words[0] != 'From' : continue
    z=words[1]
    #print(z)
    many[z] = many.get(z, 0) + 1
    largest = None
    for key, value in many.items():
        #print(key, value)
        if largest is None or value > largest:
            largest = value
            bigword = key
print(bigword, largest)
#print(many)
