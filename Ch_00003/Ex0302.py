#Input Data
hrs = input("Enter Hours:")
rate= input("Enter rate:")


try:
    # Floats
    fh=float(hrs)
    fr=float(rate)
except:print("Error, please enter numeric input!")
quit()
    
#Formula
regp=fr*fh #regular pay
otp= regp+(fh-40)*(fr*0.5) #Overtime pay

#Strings
pstregp=str(regp)
pstotp=str(otp)


if fh>40:
    print(pstotp)
else:
    print(pstregp)