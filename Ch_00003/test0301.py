y=input("Enter the Value of X: ")

try:
    x=float(y)
except:
    print("Error, please enter numeric input!")
    quit()

if x < 2 :
    print('Below 2')
elif x >= 2 :
     print('Two or more')
else :
    print('Something else')