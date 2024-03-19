fname = input('Enter file name: ')
if len(fname) < 1 : fname = ('mbox-short.txt')
fhand = open(fname)
many = dict()
strings = list(fhand)
import string
string.ascii_lowercase
alpha=list(string.ascii_lowercase)
print('STAAAAAAAAAAAAAAAA============================AAAAAAAAAAAAAAAART')
for line in strings:
    line = line.rstrip()
    line = line.lower()
    wds = line.split()
#    print(wds)
    for w in wds:
        if len(w) <2 or len(w) >7 : continue
#        if w[:]=punc:continue
        many[w] = many.get(w, 0) + 1
        print(w[:])
        d=sorted([(v,k) for k,v in many.items()], reverse = True)
        continue
#for k,v in d:
#    print('==>word',v,'    ==>value',k)
largest = None
for key, value in many.items():
    #print(key, value)
    if largest is None or value > largest:
        largest = value
        bigword = key

print('Yay! the biggest word is:', bigword, largest)
