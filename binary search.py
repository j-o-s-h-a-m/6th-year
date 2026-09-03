lst = [2, 5, 8, 12, 16, 56, 23, 72, 38, 91]
lst.sort
low = 0
high = len(list)-1
middle = (high + low)//2
target_val = 23
while low >= high:
    middle = (high + low)//2
    if lst[middle] == target_val:
        print(middle)
    elif middle > target_val:
        high = middle -1
        
    elif middle < target_val:
        low = middle + 1
       
    else:
        print('yes')
        continue
