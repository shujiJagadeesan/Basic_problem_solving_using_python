class Example():
    def __init__(self,name,address,room):
        self.name = name
        self.address = address
        self.room = room
    def occupied(self):
        print(f"Roon {self.room} at the address {self.address} is occupied by {self.name}")
s = Example("Rithik","Bharathi nagar",12)

s.occupied()

