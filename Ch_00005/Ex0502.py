largest = None
smallest = None

#Input Break and Invalid inputs
while True:
    snum = input("Enter a number: ")
    if snum == "done":
        break
    try:
        fnum=int(snum)
        if largest is None or fnum > largest :
            largest = fnum
            #print('Loop:', fnum, largest)
            #print('Largest:', largest)
        elif smallest is None or fnum < smallest :
            smallest = fnum
            #print('Loop:', fnum, smallest)
            #print('Smallest:', smallest)
        continue
    except:
        print('Invalid input')
        continue

print('Maximum is', largest)
print('Minimum is', smallest)
