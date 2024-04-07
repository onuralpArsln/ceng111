def myFunc(*args, **kwargs): 
    for arg in args:
        print("it is an arg")
        print(arg)

    for key,value in kwargs.items():
        print("kwargs")
        print("you given key")
        print(key)
        print("you given value ")
        print(value)
    

myFunc("hello"," arg", name="mamhmut",passw="123")