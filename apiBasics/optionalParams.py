def optional(a, add: int | None = None, sub: int | None= None) -> int:
    result=a
    if add != None :
        result += add
    if sub != None:
        result -=  sub

    return result


print(optional(1, add=5))
print(optional(1, sub=5))
print(optional(1, add=5, sub=7 ))
print(optional(1, add=5, sub=7 ))