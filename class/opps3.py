class customer():
    def __init__(self,c_id,name,add,phone):
        self.c_id = c_id
        self.name = name
        self.add = add
        self.phone = phone
    def setdate(self,c_id,name,add,phone):
        self.c_id = c_id
        self.name = name
        self.add = add
        self.phone = phone
    def display(self):
     return {
        'Id' : self.c_id,
        'Name' : self.name,
        'Address' : self.add,
        'Phone Number' : self.phone
     }


c1 = customer(1,'Alex','3 Street On Spot',23909009)
c = c1.display()
print(c)




        