temp = float (input ("Enter Temperature in Celcius:"))
if temp <= 0:
    print("Temperature is Freezing")
if temp > 0 and temp <= 30:
    print("Temperature is Moderate")
if temp > 30:
    print("Temperature is Hot")