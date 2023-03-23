import  datetime
import outfit as Outfit #so wird importiert
#PointofReturn: wie strukturiere ich meine Dateien, das Repository mit Packeten und imports


class Garment:
    idList = []

    #add id generator
    def __init__(self, id:int , colour:str , pattern:str, fabric:str, brand:str, size:str,  outfit:Outfit = []):
        self.id = id
        Garment.idList.append(self.id)
        self.colour = colour
        self.pattern = pattern
        self.fabric = fabric
        self.brand = brand
        self.size = size
        self.lastWear = datetime.datetime.now().date()

        self.outfit = outfit


    #TODOO    
    def addGarmentToDB(self, jsonfile):
        print("HI")
    
    #TODOO
    def deleteGarmentFromDB(self, jsonfile):
        print("BYE")

    #add ID
    def __repr__(self):
        return "Garment: Type of ({tip}), ID: {id}\n \
                colour='{col}', pattern='{pat}', fabric='{fab}', brand='{brand}', size='{size}'\n \
                Last worn: {lWear}.".format( tip = type(self), id = self.id, col = self.colour, pat = self.pattern, fab = self.fabric, brand = self.brand, size = self.size, lWear = self.lastWear)



######################################################
# Test Stationfor the class 

print(datetime.datetime.now().date())

x = Garment(1,"red","plain","cotton", None , "L")
y = Garment(2,"blue","stripes","cotton", "Nike" , "L")

print(x)

print(y)
print(type("H"))