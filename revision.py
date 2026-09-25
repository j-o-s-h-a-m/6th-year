def hola (mean):
    count = 0
    total = 0
    for i in lst:
        count += 1
        i = int(i)
        total += i
    average = total//count
    return average
        
        
    
stop = 0
lst = []
while stop == 0:
    lst_in = input('Enter the number u want to add into a list(Press enter to end input: ')
    if lst_in != '':
        lst.append(lst_in)
    else:
        break
    

average1 = hola(lst)
print(average1)
