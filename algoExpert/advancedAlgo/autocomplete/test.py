a = open("test.txt","r")
lines = a.readlines()
a.close

print(len(lines))
