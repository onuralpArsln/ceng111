import pickle
from pickleMethod import Person

#you need person class to use imported instance of  person 

with open('person.pickle', 'rb') as file:
    loaded_person = pickle.load(file)

    loaded_person.run()