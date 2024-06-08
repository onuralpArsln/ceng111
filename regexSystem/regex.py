#regex is search pattern creation

import re 

# re is a python regex package

#search a strin starts with The and ends with Spain

txt ="The rain in Spain "
x = re.search("^The.*Spain$", txt)
print(x)
"""
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string
"""
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


# \s white space demek yani boşluk
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# splits by white chracter 
txt = "The rain  in Spain"
x = re.split("\s", txt)
print(x)

# " " works but what if there is double space 
txt = "The rain in Spain"
x = re.split(" ", txt)
print(x)


# only in first occurance  the last parameter 1 makes it 
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


# replace magic 
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# replace first two
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

"""
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
