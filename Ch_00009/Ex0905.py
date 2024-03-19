fhand = open('mbox-short.txt')
many = {}
for line in fhand:
    words = line.split()
    if len(words) <= 3 or words[0] != 'From'  : continue
    emailad = words[1]
    atloc = emailad.find('@')+1
    domains = emailad[atloc:]
    many[domains] = many.get(domains, 0) + 1
    continue
print(many)
