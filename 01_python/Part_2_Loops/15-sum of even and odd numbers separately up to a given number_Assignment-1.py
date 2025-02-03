# sum of even and odd numbers separately up to a given number
num = int (input("Enter Number :"))
sum_1 = 0
sum_2 = 0
for i in range(num+1):
    if i % 2 == 0:
        sum_1 += i
print("Even Sum :",sum_1)
for j in range(num+1):
    if j % 2 != 0:
        sum_2 += j
print("Odd Sum :",sum_2)

