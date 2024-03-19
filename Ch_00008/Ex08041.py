fhand = open('romeo.txt')
data = []
for lines in fhand:
    words = lines.split()
    for word in words:
        if word not in data:
            data.append(word)
            continue
print(sorted(data))
