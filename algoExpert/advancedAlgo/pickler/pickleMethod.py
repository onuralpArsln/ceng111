# it is better to use pickle for methods 
import pickle


class Person :
    def __init__(self,  name, age ):
        self.age = age
        self.name= name 
    def run(self):
        print(f"i will run for {self.age} minutes ")



jhon = Person("jhon",34)



# wb write binary
# Serialize the object using pickle.dump()
with open('person.pickle', 'wb') as file:
    pickle.dump(jhon, file)