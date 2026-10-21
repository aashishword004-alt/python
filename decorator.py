def decorator(func):
   def wrapper():
    print('Function is Started !')
   func() 

   return wrapper

@decorator
def greet():
   print('hello world')

greet()