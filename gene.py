def numbers():
    for i in range(1, 6):
        yield i

x = numbers()

print(next(x))
print(next(x))
print(next(x))