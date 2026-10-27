# polymorphism

class dog():
    def make_sound(self):
        return 'wow!'
class cat():
     def make_sound(self):
            return 'meow!'

def sound(obj):
     print(obj.make_sound())

sound(cat())
    