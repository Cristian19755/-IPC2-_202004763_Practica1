from datetime import datetime, date, time, timedelta
import calendar
from graphviz import Digraph
class node:
    def __init__(self, data = None, siguiente = None):
        self.data = data 
        self.siguiente = siguiente

class Cola: 
    def __init__(self):
        self.root = None

    def insertar_fin(self, dato): 

        if self.root is None: 
            self.root = node(data=dato) 
            return 
        auxRoot = self.root
        while auxRoot.siguiente: 
            auxRoot = auxRoot.siguiente
        auxRoot.siguiente = node(data=dato)
    
    def imprimir_cola( self ):
        nodeAux = self.root 
        while nodeAux != None:
            print(nodeAux.data)
            nodeAux = nodeAux.siguiente

    def extraer_dato(self, x):
        auxRoot = self.root
        for i in range(0,x):
            auxRoot = auxRoot.siguiente
        return auxRoot.data

    def __str__(self):
        Cadena = "·····"
        auxRoot = self.root
        for i in range(self.cantidad_de_datos()):
            Cadena += str(auxRoot.data)
            if i != self.cantidad_de_datos()-1:
                    Cadena += str(" ")
            auxRoot = auxRoot.siguiente
        Cadena +="\n"
        return Cadena

    def cantidad_de_datos(self):
        nodeAux = self.root 
        contador= 0
        while nodeAux != None:
            contador = contador+1
            nodeAux = nodeAux.siguiente
        return contador
    
    def avanzar_cola(self):
        self.root = self.root.siguiente

class bcolors:
    ResetAll = "\033[0m"
    Bold       = "\033[1m"
    Dim        = "\033[2m"
    Underlined = "\033[4m"
    Blink      = "\033[5m"
    Reverse    = "\033[7m"
    Hidden     = "\033[8m"
    ResetBold       = "\033[21m"
    ResetDim        = "\033[22m"
    ResetUnderlined = "\033[24m"
    ResetBlink      = "\033[25m"
    ResetReverse    = "\033[27m"
    ResetHidden     = "\033[28m"

    Default      = "\033[39m"
    Black        = "\033[30m"
    Red          = "\033[31m"
    Green        = "\033[32m"
    Yellow       = "\033[33m"
    Blue         = "\033[34m"
    Magenta      = "\033[35m"
    Cyan         = "\033[36m"
    LightGray    = "\033[37m"
    DarkGray     = "\033[90m"
    LightRed     = "\033[91m"
    LightGreen   = "\033[92m"
    LightYellow  = "\033[93m"
    LightBlue    = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan    = "\033[96m"
    White        = "\033[97m"

    BackgroundDefault      = "\033[49m"
    BackgroundBlack        = "\033[40m"
    BackgroundRed          = "\033[41m"
    BackgroundGreen        = "\033[42m"
    BackgroundYellow       = "\033[43m"
    BackgroundBlue         = "\033[44m"
    BackgroundMagenta      = "\033[45m"
    BackgroundCyan         = "\033[46m"
    BackgroundLightGray    = "\033[47m"
    BackgroundDarkGray     = "\033[100m"
    BackgroundLightRed     = "\033[101m"
    BackgroundLightGreen   = "\033[102m"
    BackgroundLightYellow  = "\033[103m"
    BackgroundLightBlue    = "\033[104m"
    BackgroundLightMagenta = "\033[105m"
    BackgroundLightCyan    = "\033[106m"
    BackgroundWhite        = "\033[107m"

class MAIN:
    def menu(self):
        if ordenes.cantidad_de_datos() == 0:
            print(bcolors.Red+'(Actualmente la cola esta vacia)'+bcolors.ResetAll)
        print('------Seleccione una opcion------')
        print('   1.Datos del desarrollador')
        print('   2.Mostrar cola de ordenes')
        print('   3.Agregar orden')
        print('   4.Finalizar siguiente orden')
        print('   5.Salir')
        op = int(input())
        if op == 1:
            print(bcolors.Red+'::::::::::::::::::' +bcolors.ResetAll+'Datos del desarrollador'+ bcolors.Red+'::::::::::::::::::' +bcolors.ResetAll)
            print('--- '+bcolors.Blue+'Introducción a la programacion y computación 2 sección "A"'+bcolors.ResetAll)
            print('--- '+bcolors.Blue+'Cristian Noé Axpuac Aspuac'+bcolors.ResetAll)
            print('--- '+bcolors.Blue+'202004763\n'+bcolors.ResetAll)
            M.menu()
        elif op == 2:
            M.graficar()
            print('-----Grafica de cola genrada con exito-----\n')
            M.menu()
        elif op == 3:
            print(bcolors.Yellow +'|/|\|/|\|/|'+ bcolors.White+'Ingrese la cantidad de pizzas a solicitar'+ bcolors.Yellow +'|/|\|/|\|/|' +bcolors.ResetAll)
            NpizzasPep = int(input('De peperoni: '))
            NpizzasSal = int(input('De Salchicha: '))
            NpizzasCar = int(input('De Carne: '))
            NpizzasQue = int(input('De Queso: '))
            NpizzasPiñ = int(input('De Piña: '))
            M.insertar_orden(NpizzasPep, NpizzasSal, NpizzasCar, NpizzasQue, NpizzasPiñ) 
        elif op == 4:
            M.avanzar_cola_ordenes()
        elif op == 5:
            exit()
    
    def graficar(self):
        h = Digraph('G', filename='ColaDeOrdenes.gv', format ='png',
                        edge_attr={'color': 'orange:red', 'style': 'filled'})
        h.attr('node', shape='diamond', style='filled', color='violet:blue')
        for i in range(0,ordenes.cantidad_de_datos()):
            if i == 0:
                y = str(ordenes.extraer_dato(0))
                h.node(y)
            else:
                x = str(ordenes.extraer_dato(i))
                z = str(ordenes.extraer_dato(i-1))
                h.node(x)
                h.edge(x,z)
            if i == ordenes.cantidad_de_datos()-1:
                h.attr('node', shape='box', style='filled', color='green:yellow', fontcolor='black')
                inicio = 'Siguiente orden'
                h.node(inicio)
                h.edge(inicio, y)
        h.view()

    def insertar_orden(self, peperoni, salchicha, carne, queso, piña):
        orden1 = Cola()
        tiempoproceso = int(peperoni)*3 + int(salchicha)*4 + int(carne) * 10 + int(queso )*5 + int(piña)*2
        horaf = datetime.now().hour
        minutosf = datetime.now().minute
        tiempoproceso = minutosf + tiempoproceso
        while tiempoproceso >= 60:
            horaf = horaf+1
            tiempoproceso = tiempoproceso-60
        tiempoproceso = str(horaf)+'·'+str(tiempoproceso)

        orden = ' Orden '
        peperoniL = '\n     Peperoni ' + str(peperoni) 
        salchichaL = '\n     Salchicha ' + str(salchicha)
        carneL = '\n     Carne ' + str(carne)
        quesoL = '\n     Queso ' +str(queso)
        piñaL = '\n     Piña '+ str(piña)        
        hora = '\n     Hora de ingreso '+str(datetime.now().strftime('%H·%M'))+'.'
        te= '\n     Hora estimada de salida '+ str(tiempoproceso) + '.'
        
        orden1.insertar_fin(orden)
        if peperoni != 0:
            orden1.insertar_fin(peperoniL)
        if salchicha != 0:
            orden1.insertar_fin(salchichaL)
        if carne != 0:
            orden1.insertar_fin(carneL)
        if queso != 0:
            orden1.insertar_fin(quesoL)
        if piña != 0:
            orden1.insertar_fin(piñaL)
        
        orden1.insertar_fin(hora)
        orden1.insertar_fin(te)
        tiempo.insertar_fin(tiempoproceso)
        ordenes.insertar_fin(orden1)
        print('----- Orden ingresada exitosamente -----')
        print(orden1)
        M.menu()

    def avanzar_cola_ordenes(self):
        tiempofinal = str(datetime.now().hour)+':'+str(datetime.now().minute)
        print('···· Orden Finalizada')
        print(ordenes.extraer_dato(0))
        print('Hora de salida de la orden: '+tiempofinal)
        ordenes.avanzar_cola()
        M.menu()

M = MAIN()
ordenes = Cola()
tiempo = Cola()
tiempoi = Cola()
M.menu()