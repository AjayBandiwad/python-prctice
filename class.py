class truck:
    #properties
    seat = 2
    tyre = 6
    fule = "D"
    carrier = "Goods"
    fuelstate = "true"
    
    #methods
    def drive(self):
        if self.fuelstate == True:
            print("Ready to Drive , Fuel is Available")
        else:
            print("No Fuel is Available")
            
    def __init__(self,seat,tyre):
        self.seat = seat
        self.tyre = tyre
        self.fuel = "petrol"
        self.carrier = "Frozen Goods"
        self.fuelstate = False