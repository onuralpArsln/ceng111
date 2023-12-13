hull=[]
bridge=[]
quarters=[]

locations=[hull,bridge,quarters]

objs=[]
crew = []


class Personel():
    spcies = "clone"
    armor = "light"
    weapon =  "laser"
    location = "hull"
    

    def __init__(self, name) -> None:
        self.name= name
        crew.append(self.name)
        hull.append(self.name) 
        objs.append(self)

    def battleCry(self):
        print("Hurrraaa")

    def whoAmI(self):
        print(f"I am {self.name} a clone with light armor and laser weapon")

    def getUpgrades(self):
        self.weapon   = "Kinetic"
        self.armor = "Heavy"

    def rest(self):
        self.location="quarters"
        for loc in locations:
            if self.name in loc:
                loc.remove(self.name)
        quarters.append(self.name)

    def toBattleStaion(self):
        self.location="hull"
        for loc in locations:
            if self.name in loc:
                loc.remove(self.name)
        hull.append(self.name)




class Captain(Personel):
    rank="Captain"

    def __init__(self,name,exp):
        super().__init__(name)
        self.exp = exp

    def toBattleStaion(self):
        self.location="bridge"
        for loc in locations:
            if self.name in loc:
                loc.remove(self.name)
        bridge.append(self.name)


    def battleCry(self):
        print("Forwarddd!!!!")




class ArmsMaster(Personel):

    def upgradePersonel(self,obj):
        obj.weapon = "BigGuns"