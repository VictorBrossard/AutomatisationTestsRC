class Base(object): 
 
    # Constructeur
    def __init__(self, nom): 
        self.nom = nom 
   
    # retourner le nom 
    def getNom(self): 
        return self.nom 
   
   
class Child(Base): 
       
    # Constructeur
    def __init__(self, nom, age): 
        Base.__init__(self, nom) 
        self.age = age 
   
    # retourner l'age 
    def getAge(self): 
        return self.age 
   
class GrandChild(Child): 
       
    # Constructeur
    def __init__(self, nom, age, adresse): 
        Child.__init__(self, nom, age) 
        print("innn")
        self.adresse = adresse 
   
    # retourner l'adresse
    def getAdresse(self): 
        return self.adresse         
   
# tester le code
g = GrandChild("ISMAIL", 32, "Meknes")   
print(g.getNom(), g.getAge(), g.getAdresse()) 