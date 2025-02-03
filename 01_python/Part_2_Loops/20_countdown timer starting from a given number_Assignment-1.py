import time
sec = int(input("Enter Seconds in numbers:"))
for i in range(sec,0,-1):
    print(i)
    time.sleep(1)
print("Time Up")