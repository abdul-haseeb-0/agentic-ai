num = input("Enter Number:")
arr_num = []
for i in num:
    arr_num.append(i)
l = 0
r = len(arr_num)-1
while l < r:
    arr_num[l] , arr_num[r] = arr_num[r] , arr_num[l]
    l += 1 
    r -= 1
rev_num = ''.join(arr_num)
print(rev_num)