class Star:

    type = 'Star'
    x = 100

    def change():
        x = 200
        print('X is ', x)

print('x IS ', Star.x)
Star.change()
print('x IS ',Star.x)

star = Star()
print('x IS ', star.x)
star.change()