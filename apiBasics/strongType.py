def valueSorter(a : int) -> int :
    #this function must take and int and return one 
    b=[0,"1bir"]
    return b[a]


#works since it takes an int and return an int
print(valueSorter(0))


# it wont fail since ->int only gives a info about return type but not enforces it 
print(type(valueSorter(1)))