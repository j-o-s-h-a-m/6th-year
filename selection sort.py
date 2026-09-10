lst = [4 , 2 , 1 , 9 , 10]

temp = 0
for i in range(0,len(lst)-1):
    temp = lst[i + 1]
    if lst[i] > lst[i+1] :
        lst[i+1] = lst[i]
        lst[i] = temp
    else :
        continue
for i in range(0,len(lst)-1):
    temp = lst[i + 1]
    if lst[i] > lst[i+1] :
        lst[i+1] = lst[i]
        lst[i] = temp
    else :
        continue
print(lst)
