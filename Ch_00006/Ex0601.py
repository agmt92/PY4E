str = 'X-DSPAM-Confidence: 0.8475'
a1 = str.find(':')
a2 = str[a1+1:]
a3 = float(a2)
print(a3)
