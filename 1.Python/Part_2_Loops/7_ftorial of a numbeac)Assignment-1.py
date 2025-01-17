num = int (input("Enter Number : "))
i = 1
fact = 1
while i < num+1 :
    fact = fact * i
    i += 1
print(f"Factorial of {num} = {fact}")