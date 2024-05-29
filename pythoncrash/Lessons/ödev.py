class Araba:
    
    def __init__(self,marka,renk):
        self.marka= marka 
        self.renk=renk

    def total_people(self):
        return "max: 6 people"

    def max_speed(self):
        return "max: 200 km/h"
    
class Yarışarabası(Araba):
    
    def __init__(self,marka,renk):
        super().__init__(marka,renk)
    
    def max_speed(self):
        return "yarış arabasının max speed 200 km/h"

class Minibüs(Araba):
    
    def __init__(self, marka, renk):
        super().__init__(marka, renk)
    
    def total_people(self):
        return "Minibüs max 6 kişi alabilir" #super().total_people() otomatik böyle yazdı damnn 


#4 methodu olsun,verilen isimle txt dosyası oluşturma,içini okuma,dosyaya yazma,ekleme





