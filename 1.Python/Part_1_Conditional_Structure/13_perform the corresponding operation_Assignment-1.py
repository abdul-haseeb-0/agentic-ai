num_1 = float (input("Enter First Number:"))
num_2 = float (input("Enter Second Number:"))
opt = (input("Enter Operator:"))
if opt == "+" :
    print(num_1 + num_2)
elif opt == "-" :
    print(num_1 - num_2)
elif opt == "*" :
    print(num_1 * num_2)
elif opt == "/" :
    print(num_1 / num_2)
elif opt == "%" :
    print(num_1 % num_2)
else:
    print("Invalid operator")
