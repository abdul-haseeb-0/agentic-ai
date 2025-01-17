# for i in range(1,5,1):
#     for j in range(5-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end="")
# Number of rows for the pyramid
rows = 5

# Outer loop for each row
for i in range(rows):
    # Inner loop for spaces
    for j in range(rows - i - 1):
        print(" ", end="")
    # Inner loop for stars
    for k in range(2 * i + 1):
        print("*", end="")
    # Move to the next line after each row
    print()
