Class Cars():
pass

Maruti = Cars()
Hyundai = Cars()

Maruti.Model = "Baleno"
Maruti.Color = "White"
Maruti.Exprice = 800000

Hyundai.Model = "i20"
Hyundai.Color = "Black"
Hyundai.Exprice = 900000

print(Maruti.Model)
print(Hyundai.Model)



class Cars():
    def __init__(self,Model,Color,Exprice):
        self.Model = Model
        self.Color = Color
        self.Exprice = Exprice

Maruti = Cars("Baleno","White","800000")
Hyundai = Cars("i20","Black","900000")

print(Maruti.Model)
Print(Hyundai.Model)