print ("merhaba")

##KÖTÜ ÖRNEK 

def funCalc(a,b):
        b=a*b
        return a+b

def funAdd(a,b=15):
        '''eğer b değeri verilirse funAdd(1,2) verilen değeri kullan ama verilmezse funAdd(1) b için 15 kullan'''
        return a +  b 


print(funCalc(2,3))