num = int (input ("Enter Number :"))
rlt = 0
while num != 0:
    num = num // 10
    rlt += 1
print(rlt)