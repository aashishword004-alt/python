class father():
     def display(self):
         print('this from perents class')


class child(father):
     
     def display(self):
          super().display()
          print('this is child class')
         


c=child()
c.display()
          
     