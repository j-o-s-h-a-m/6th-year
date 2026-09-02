#Author - Saksham Joshi
#Date - 02 september 2026

lst = []

a = 0
while a == 0 :
    list1 = list(input("Enter element for your list: "))
    lst = lst + list1
    if list1 == [] :
        break
x = input("enter the element you want to find in the list: ")
index = lst.index(x)
print(index)
