var1=10 
var2=30
print("merhaba")

def func1(a,b=2):
    print(a*b)



# import edilen module çalıştırılır 
# eğer modulun import edildiyse __name__ değişkeni dosya adı olur ve bu
# kod çalışır
if __name__ == "file1":
    print("meraba ben importum") 

# eğer modulu direkt çalıştırdıysan __name__ __main__ olacağı için buırası çalışır
if __name__ == "__main__" :
    print(__name__)
    print("şuan file1 çalışıyor")