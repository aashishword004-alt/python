#inheritance in python
class employee:
    def majdoore(self):
        print('Employee is Working')

class developer(employee):
     def write_code(self):
         print('Developer is writing Code')

m = developer()
m.majdoore()
m.write_code()