def hola (mean):
    count = 0
    total = 0
    for i in lst:
        count += 1
        i = int(i)
        total += i
    average = total//count
    return average
def hola1(median):
    n = length
    if n%2 == 0:
        med = ((n/2)+((n/2)+1))//2
    else:
        med = (n+1)/2
    return med
def hola3(mode):
    count = 0
    highest = 0
    larget = 0
    for i in lst:
        count = lst.count(i)
        if count >= highest:
            largest = i
            highest = count
    return highest, largest
    
    
    

lst = [1,2,3,3,4,5]
length = len(lst)
median1 = hola1(lst)
average1 = hola(lst)
mode1 = hola3(lst)
print(average1)
print(median1)
print(mode1)

