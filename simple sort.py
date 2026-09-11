lst = [9,8,7,6,5,4,2,13]
lst1 = []
length = len(lst)-1
lowest = lst[0]
while lst != []:
    smallest = lst[0]
    for i in range(0,length):
        if lst[i]< smallest:
            smallest = lst[i]
    lst1.append(smallest)
    lst.remove(smallest)
    length = len(lst)-1
print(lst1)
