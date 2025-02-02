user_input = input ("Enter String Value:")
if user_input.isupper() :
    print (user_input,"is in Upper Case")
elif user_input.islower():
    print (user_input,"is in Lower Case")
else:
    print (user_input,"is in Mix Case")