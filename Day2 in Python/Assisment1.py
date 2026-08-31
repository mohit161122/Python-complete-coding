Selery = int(input("Enter the Selery :"))

if (Selery < 30000):
    print("Final tax rate is 5%")
elif(Selery > 30000 and Selery <= 70000):
    print("Final tax rate is 15%")
else:
    print("Final tax rate is 25%")