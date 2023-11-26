
# exampleb deki sadece funcalcı al buraya getir 
from exampleB import funCalc, funAdd
#böyle importlarsan fonksiyon adı çağırma için yeterli


import exampleA
#böyle importlarsan modüladı.fonksiyonadı yazman lazımm
exampleA.funCalc(3,4)


# examplea deki her fonksiyonu al buraya getir 
from exampleA import * 



print(funCalc(2,5))
print(funAdd(1))
print(funAdd(1,2))


