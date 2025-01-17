num_2 = int(input("Enter Second Number:"))
num_1 = int(input("Enter First Number:"))
num_3 = int(input("Enter Third Number:"))
if num_1 > num_2 and num_1 > num_3 :
    print (f"{num_1} is greater than {num_2} and {num_3}")
elif num_2 > num_3 and num_2 > num_3 :
    print (f"{num_2} is greater than {num_1} and {num_3}")
elif num_3 > num_1 and num_3 > num_1 :
    print (f"{num_3} is greater than {num_1} and {num_2}")
elif num_1 == num_2 == num_3:
    print (" You Entered Same Numbers ")
else:
    print (" Invalid Input ")