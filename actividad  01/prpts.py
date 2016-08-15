#prprties experiments

class Circulo:

    def __init__(self, c, r):
        self.centro = c
        self.radio = r

    #
    def getc(self):
        return self.centro

    def setc(self, nc):
        self.centro = nc

    def delc(self):
        del self.centro

    center = property(getc, setc, delc)
    #

    #
    def getr(self):
        return self.radio

    def setr(self, nr):
        self.radio = nr

    def delr(self):
        del self.radio

    radius = property(getr, setr, delr)
    #

    #sintaxis alternativa (ejmplo con self.centro)
    '''
    @property
    def center(self):
        return self.centro
    @center.setter
    def center(self, nc):
        self.centro = nc
    @center.deleter
    def center(self):
        del self.centro
    '''


circ1 = Circulo((3,2), 1)
print('#')
print(circ1.centro)
print(circ1.radio)

'''#forma sin properties
circ1.setc((-1,-2))
print('#')
print(circ1.centro)
print(circ1.radio)
'''

#forma con properites
circ1.center = (7,7)
circ1.radius = 99
print('#')
print(circ1.centro)
print(circ1.radio)
del circ1

###