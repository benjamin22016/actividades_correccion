# actividad 1 benjamin22016
import datetime


class Automotora:

    def __init__(self, nombre, sucursales):
        self.nombre = nombre
        self.sucursales = sucursales

    def agregarSucursal(self, sucursal):
        self.sucursales.append(sucursal)


class Sucursal:

    def __init__(self, nombre, autos_usados, autos_nuevos):
        self.nombre = nombre
        self.autos_usados = autos_usados
        self.autos_nuevos = autos_nuevos

    def agregarAuto(self, auto):
        if auto.estado == 'usado':
            self.autos_usados.append(auto)
        elif auto.estado == 'nuevo':
            self.autos_nuevos.append(auto)


class Auto:

    def __init__(self, id, marca, año, modelo, transmision, precio, estado, dueño, nc=0, uc=None):
        self.id = id
        self.marca = marca
        self.año = año
        self.modelo = modelo
        self.transmision = transmision
        self.precio = precio
        self.estado = estado
        self.dueño = dueño
        self.nconsultas = nc
        self.uconsultas = uc

    def get_uconsulta(self):
        return self.uconsulta
    def set_uconsulta(self, nueva_uconsulta):
        self.uconsulta = nueva_uconsulta
    def del_uconsulta(self):
        del self.uconsulta
    last_date = property(get_uconsulta, set_uconsulta, del_uconsulta)

    def get_precio(self):
        return self.precio
    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    def del_precio(self):
        del self.precio
    price = property(get_precio, set_precio, del_precio, "price propiedad de precio")

    def desplegar(self):

        self.nconsultas = self.nconsultas + 1
        self.last_date = datetime.datetime.now()

        if self.dueño == '':
            print(str(self.id) + ', ' + str(self.marca) + ', ' + str(self.año) + ', ' + str(self.modelo) + ', ' + str(self.transmision) + ', '
                  + str(self.price) + ', ' + str(self.estado) + ', ' + str(self.nconsultas) + ', ' + str(self.last_date))
        else:
            print(str(self.id) + ', ' + str(self.marca) + ', ' + str(self.año) + ', ' + str(self.modelo) + ', ' + str(self.transmision) + ', '
                  + str(self.price) + ', ' + str(self.estado) + ', ' + str(self.dueño.nombre) + ', ' + str(self.nconsultas) + ', ' + str(self.last_date))


class Dueño:

    def __init__(self, nombre, rut, telefono, correo):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono
        self.correo = correo


# creando objetos
dueño1 = Dueño('pedro', 11, 123, 'pepe@gmail.com')
dueño2 = Dueño('juan', 22, 456, 'juan@gmail.com')
dueño3 = Dueño('diego', 33, 789, 'diego@gmail.com')

dueño4 = Dueño('moe', 44, 101, 'moe@gmail.com')
dueño5 = Dueño('larry', 55, 112, 'larry@gmail.com')
dueño6 = Dueño('joe', 66, 131, 'joe@gmail.com')

auto1 = Auto(1, 'ford', 2016, 'mustang', 'AT', 20000000, 'nuevo', '')
auto2 = Auto(2, 'chevrolet', 2016, 'camaro', 'MT', 25000000, 'nuevo', '')
auto3 = Auto(3, 'ferrari', 2016, 'lambo', 'AT', 100000000, 'nuevo', '')

auto4 = Auto(4, 'ford', 2014, 'mustang', 'MT', 15000000, 'usado', dueño1)
auto5 = Auto(5, 'chevrolet', 2012, 'camaro', 'MT', 18000000, 'usado', dueño2)
auto6 = Auto(6, 'ferrari', 2010, 'lambo', 'AT', 75000000, 'usado', dueño3)

auto7 = Auto(7, 'ford', 2016, 'mustang', 'AT', 20000000, 'nuevo', '')
auto8 = Auto(8, 'chevrolet', 2016, 'camaro', 'MT', 25000000, 'nuevo', '')
auto9 = Auto(9, 'ferrari', 2016, 'lambo', 'AT', 100000000, 'nuevo', '')

auto10 = Auto(10, 'ford', 2014, 'mustang', 'MT', 15000000, 'usado', dueño4)
auto11 = Auto(11, 'chevrolet', 2012, 'camaro', 'MT', 18000000, 'usado', dueño5)
auto12 = Auto(12, 'ferrari', 2010, 'lambo', 'AT', 75000000, 'usado', dueño6)

sucursal1 = Sucursal('Surusal1', [], [])
sucursal2 = Sucursal('Surusal2', [], [])

automotora1 = Automotora('Mavrakis', [])
#

# set up
A = []
A.append(automotora1)

sucursal1.agregarAuto(auto1)
sucursal1.agregarAuto(auto2)
sucursal1.agregarAuto(auto3)
sucursal1.agregarAuto(auto4)
sucursal1.agregarAuto(auto5)
sucursal1.agregarAuto(auto6)

sucursal2.agregarAuto(auto7)
sucursal2.agregarAuto(auto8)
sucursal2.agregarAuto(auto9)
sucursal2.agregarAuto(auto10)
sucursal2.agregarAuto(auto11)
sucursal2.agregarAuto(auto12)

automotora1.agregarSucursal(sucursal1)
automotora1.agregarSucursal(sucursal2)
#

# menu
switch = 1
while switch == 1:
    o1 = int(input('trabajador(1) | usuario(2): '))

    if o1 == 1:

        o2 = int(input('cambiar precio(1) | desplegar el numero de autos(2) : '))

        if o2 == 1:

            nid = int(input('ingrese el id del auto: '))
            np = int(input('ingrese el nuevo precio: '))

            for i in range(len(A)):
                S = A[i].sucursales
                for j in range(len(S)):

                    U = S[j].autos_usados
                    for k in range(len(U)):
                        if U[k].id == nid:
                            U[k].price = np

                    N = S[j].autos_nuevos
                    for k in range(len(N)):
                        if N[k].id == nid:
                            N[k].price = np

        elif o2 == 2:

            nt = 0

            for i in range(len(A)):
                S = A[i].sucursales
                for j in range(len(S)):
                    U = S[j].autos_usados
                    nt = nt + len(U)
                    N = S[j].autos_nuevos
                    nt = nt + len(N)

            print(nt)

    elif o1 == 2:
        o2 = int(input('consultar segun año(1) | precio(2) | marca(3) | transmision(4) | estado(5): '))

        if o2 == 1:
            p1 = int(input('año inferior: '))
            p2 = int(input('año superior: '))

            for i in range(len(A)):
                S = A[i].sucursales
                #print(S)
                for j in range(len(S)):
                    U = S[j].autos_usados
                    #print(U)
                    N = S[j].autos_nuevos
                    #print(N)
                    for ak in range(len(U)):
                        p = U[ak].año
                        #print(p)
                        if (p1 <= p) and (p <= p2):
                            U[ak].desplegar()
                            #print('#1')
                    for bk in range(len(N)):
                        p = N[bk].año
                        if (p1 <= p) and (p <= p2):
                            N[bk].desplegar()
                            #print('#2')

        elif o2 == 2:
            p1 = int(input('precio inferior: '))
            p2 = int(input('precio superior: '))

            for i in range(len(A)):
                S = A[i].sucursales
                for j in range(len(S)):
                    U = S[j].autos_usados
                    N = S[j].autos_nuevos
                    for ak in range(len(U)):
                        p = U[ak].precio
                        if (p1 <= p) and (p <= p2):
                            U[ak].desplegar()
                    for bk in range(len(N)):
                        p = N[bk].precio
                        if (p1 <= p) and (p <= p2):
                            N[bk].desplegar()

        elif o2 == 3:
            marca = input('ingrese marca: ')
            for i in range(len(A)):
                S = A[i].sucursales
                for j in range(len(S)):
                    U = S[j].autos_usados
                    N = S[j].autos_nuevos
                    for ak in range(len(U)):
                        p = U[ak].marca
                        if marca == p:
                            U[ak].desplegar()
                    for bk in range(len(N)):
                        p = N[bk].marca
                        if marca == p:
                            N[bk].desplegar()

        elif o2 == 4:
            trans = input('ingrese transmision: ')
            for i in range(len(A)):
                S = A[i].sucursales
                for j in range(len(S)):
                    U = S[j].autos_usados
                    N = S[j].autos_nuevos
                    for ak in range(len(U)):
                        p = U[ak].transmision
                        if trans == p:
                            U[ak].desplegar()
                    for bk in range(len(N)):
                        p = N[bk].transmision
                        if trans == p:
                            N[bk].desplegar()

        elif o2 == 5:
            estado = input('ingrese estado: ')
            for i in range(len(A)):
                S = A[i].sucursales
                for j in range(len(S)):
                    U = S[j].autos_usados
                    N = S[j].autos_nuevos
                    for ak in range(len(U)):
                        p = U[ak].estado
                        if estado == p:
                            U[ak].desplegar()
                    for bk in range(len(N)):
                        p = N[bk].estado
                        if estado == p:
                            N[bk].desplegar()

###