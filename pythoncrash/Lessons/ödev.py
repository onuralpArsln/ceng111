class Car:
    
    def __init__(self,brand,color):
        self.brand= brand 
        self.color= color

    def total_people(self):
        return "max: 6 people"

    def max_speed(self):
        return "max: 200 km/h"
    
class RaceCar(Car):
    
    def __init__(self,brand,color):
        super().__init__(brand,color)
    
    def max_speed(self):
        return "yarış arabasının max speed 200 km/h"

class Minicar(Car):
    
    def __init__(self, brand, color):
        super().__init__(brand, color)
    
    def total_people(self):
        return "Minibüs max 6 kişi alabilir" #super().total_people() otomatik böyle yazdı damnn 


#4 methodu olsun,verilen isimle txt dosyası oluşturma,içini okuma,dosyaya yazma,ekleme
class FileManager:
    def __init__(self,file_name):
        self.file_name= file_name
    
    def create_file(self):
        with open(self.file_name, "r") as file:
            pass
    def read_file(self):
        try:
            with open(self.file_name, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Can't find file"
        

    def write_file(self):
     
    def append_file(self):

   


