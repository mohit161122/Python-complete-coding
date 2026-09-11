Selery = int(input("Enter your Selery :"))

if( Selery <= 30000):
    print("Tax rate is 5%")
elif(Selery > 30000 and Selery <= 70000):
    print("Tax rate is 15%")
else:
    print("Tax  rate is 25%")