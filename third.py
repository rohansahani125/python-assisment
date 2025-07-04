def first_unique_char(s: str) -> str:
    x = []
    repeated = []
    for i in s:
        if i in repeated:
            continue
        if i in x:
            repeated.append(i)
            x.remove(i)
        else:
            x.append(i)

    if x:
        return x[0]  # return the first unique character
    else:
        return "None"


        
#Example:
s = "swiss"
print(first_unique_char(s)) 