fhand = open('mbox-short.txt')
count = 0
tot = float()
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        snum = float(line[20:])
        count = count+1
        tot = tot + snum
        #print(snum)
        continue


aver = tot/count
#print('sum', tot)
#print('count', count)
print('Average spam confidence: ', aver)
print(tot)
