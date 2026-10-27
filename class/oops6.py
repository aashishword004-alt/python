class father():
     def display(self):
         print('this from father  class')

class mother():
     def display(self):
          print('this from mother class')

class child(father,mother):
      def display(self):
          mother().display()
          father().display()
          print('this is child class')


c1 = child()
c1.display()