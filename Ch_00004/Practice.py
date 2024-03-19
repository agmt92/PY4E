#Create function
def computepay(rate, hours):
    if hours>40:
        regp=rate*hours
        otp=(hours-40)*(rate*0.5)
        pay=regp+otp
    else:
        pay=rate*hours
    return(pay)

#Input Strings
sth = input("Enter hours:")
str = input("Enter rate:")
#Floats
fh = float(sth)
fr = float(str)
xp = computepay(fr, fh)
#print
print("Pay", xp)
