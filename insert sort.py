#Author = saksham Joshi
#date = 23 / 09 / 2026
lst = [11 , 7 , 14 , 19 ,12,1,2,-5]

marker = 0

for i in range(1,len(lst)):
    marker= lst[i]
    for j in range(i-1,-1,-1):
        if lst[j] > marker:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)
