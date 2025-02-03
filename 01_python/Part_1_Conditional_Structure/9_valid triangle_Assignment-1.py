hyp = float (input("Enter Length of Side 1 :"))
base = float (input("Enter Length of Side 2 :"))
alt = float (input("Enter Length of Side 3 :"))
if hyp + base > alt and alt + base > hyp and hyp + alt > base:
    print("Valid Triangle")
else:
    print ("Invalid Triangle")