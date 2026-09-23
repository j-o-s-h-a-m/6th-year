#Author = saksham Joshi
#date = 23 / 09 / 2026
lst = [11 , 7 , 14 , 19 ,12]

stop = 0
val1 = 0
val2 = 0

while stop == 0:
    for i in range(0,len(lst)-1):
        if lst[i] > lst[i+1]:
            val1 = lst[i]
            val2 = lst[i+1]
            lst[i] = val2
            lst[i+1] = val1
    lst1 = lst
    if lst1 == lst:
        stop = 1
    print(lst)
    
    
            
            
