fname = input('Enter file name: ')
if len(fname) < 1 : fname = ('clown.txt')
fhand = open(fname)
many = dict()
for line in fhand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        many[w] = many.get(w, 0) + 1
#print(many)
largest = None
for key, value in many.items():
    #print(key, value)
    if largest is None or value > largest:
        largest = value
        bigword = key

print('Yay!:', bigword, largest)
