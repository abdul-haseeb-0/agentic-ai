age = int( input("Enter Your AGE :" ))
if age < 18:
    print("Minor")
elif age >= 18 and age < 60:
    print("Adult")
else:
    print ("Senior Citizen")