def find_missing_number(arr: list) -> int:
    x = arr
    y = 1
    z = len(x)
    k = 1
    
#as our list start with 0, we can check if it has 0 seperately    
    if 0 not in x:
        return 0

#for all the other numbers this loop will help
    for i in x:
        if i == 0:
            pass
        else:
            y *= i
    
    for i in range (z):
        k *= i+1

    j = k/y

    return int(j)


arr =[3,0,1]

print(find_missing_number(arr)) 

