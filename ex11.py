class Compte :

    # def __init__(self, rib , sold , NomClient) :
    #     self.rib = rib
    #     self.sold = sold
    #     self.NomClient = NomClient
    
    rib = ''
    sold = 0.0
    NomClient = ''


    def Setsaisie (self) :
        self.rib=str(input("entrer votre rib :\n"))
        self.sold=float(input("entrer votre sold :\n"))
        self.NomClient = str (input("votre nom :\n"))

    def Setdepot (self , montantA) :
        self.sold =  montantA 
        self.sold = self.sold + montantA 
        return self.Setdepot
    
    def Getretrait ( self , montantA ) :
        self.sold = montantA
        self.sold = self.sold - montantA

C = Compte()
C.Setsaisie()
C.Setdepot()
C.Getretrait(

)