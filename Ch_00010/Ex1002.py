fhand = open('mbox-short.txt')
many = {}
for line in fhand:
    words = line.split()
    if len(words) <= 3 or words[0] != 'From'  : continue
    emailad = (words[5])
    z = line.find(':')
    a = z-2
    s = line[a:z]
    many[s] = many.get(s, 0) + 1
    d=(sorted([(k,v) for k,v in many.items()]))
    print(s)
    continue
#for k,v in d:
#    print(k,v)
