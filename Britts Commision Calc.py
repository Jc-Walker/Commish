x  = int(input("Total monthly revenue: "))
y = 0
if (x <= 10000):
    print ("Commission on $", x," is $", y)
elif x <= 25000:
    print("Commission on $", x," is $", y+((x-10000)*0.08))

elif x <= 35000:
    print("Commission on $", x," is $", y+(((x - 25000)*0.1)+1200))

elif (x <= 45000):
    print("Commission on $", x," is $", y+(((x - 35000)*0.125)+2200))

elif (x > 45000):
    print("Commission on $", x," is $", y+(((x - 45000)*0.15)+3450))
