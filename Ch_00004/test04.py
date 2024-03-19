def computepay(rate, hours):
    if hours>40:
        regp=rate*hours #regular pay
        otp=(hours-40)*(rate*0.5) #Overtime pay
        pay=regp+otp
    else:
        pay=rate*hours
    return(pay)

#Input Data
sh = input("Enter Hours:")
sr = input("Enter rate:")
# Floats
fh = float(sh)
fr = float(sr)
#Insert function
xp = computepay(fr, fh)
print("Pay", xp)
