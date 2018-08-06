z = input('specific gravity wanted: ')
z = float(z)

x1 = 1.830
x2 = 1

y1 = 1.00
y2= 1


while (((x1*x2) + (y1*y2)) / (x2+y2)) != z:
    if (((x1*x2) + (y1*y2)) / (x2+y2)) > z:
        y2 += 1
    if (((x1*x2) + (y1*y2)) / (x2+y2)) < z:
        x2 += 1

print((((x1*x2) + (y1*y2)) / (x2+y2)))
print('Parts sulfuric acid: ',x2,'\nParts water: ',y2)
