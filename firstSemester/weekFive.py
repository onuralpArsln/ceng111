
# exampleb deki sadece funcalcı al buraya getir 
from exampleB import funCalc
#böyle importlarsan fonksiyon adı çağırma için yeterli


import exampleA
#böyle importlarsan modüladı.fonksiyonadı yazman lazımm
exampleA.funCalc(3,4)


# examplea deki her fonksiyonu al buraya getir 
from exampleA import * 

 # importladığın modül değişkenlerine ulaşabilrsin
import exampleGlobalvar


print(f'global var is {exampleGlobalvar.a}')
exampleGlobalvar.a  = exampleA.funAdd(5)
print(f'global var is {exampleGlobalvar.a}')


print(funCalc(2,5))
print(funAdd(1))
print(funAdd(1,2))


