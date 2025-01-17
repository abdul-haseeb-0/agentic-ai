S1 = int( input (" Enter First side :")) 
S2 = int( input (" Enter second side :")) 
S3 = int( input (" Enter Third side :")) 
if S1 == S2 or S2 == S3 or S1 == S3 :
    print ("Isoceles Triangle")
elif S1 != S2 and S2 != S3 and S1 != S3 :
    print ("Scalene Triangle")
else:
    print ("Scalene Triangle")