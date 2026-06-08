#Reverse an array

lst = [2,4,6,8]
lst1=[]

list_len = len(lst)

while(list_len>0):
    lst1.append(lst[list_len-1])
    list_len-=1
    
print(lst1)