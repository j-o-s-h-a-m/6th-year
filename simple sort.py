lst = [ 1 , 0 , 4 , 3 , 9 , 7]
lst1 = []
length = len(lst)
lowest = lst[0]
while lst != []:
#     for j in range(0,length-1):
        for i in range(0,length-1):
            if lst[i] < lst[i+1]:
                lowest = lst[i]
                
            lst1.append(lowest)
            lst.pop(lst[i])
            print(lst1)
        length = len(lst)
        lowest = lst[0]
