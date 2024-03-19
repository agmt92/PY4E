fhand = open('romeo.txt')
count = 0
tot = 0
for line in fhand:
    words = line.split()
    line = line.rstrip()
    l = len(line)
    tot = tot + l
    #print(line)
    continue
print(tot)
