x = input("put your number in here")

try:
    xint = int(x)
    print("I am working", x)
except:
    print("something broke")
	
if xint > 0:
    xval = "Positive"
elif xint == 0:
    xval = "Zero"
else:
    xval = "Negative"
	
if xint % 2 == 0:
    xpolar = "Even"
else:
    xpolar = "Odd"
	
if xval is "Positive":
    y = 1
elif xval is "Negative":
    y = -1
else:
    y = 0
	
while xint != y:
    y = y + (y*1)/abs(y)
    print("Counting...at current number:", y)
	
print("Your number is:",xval,"and",xpolar,"and the number is:",y)
	
