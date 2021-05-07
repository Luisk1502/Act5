# Nombre: Luis Carlos Balderramama
# Matricula: A00226908
# Reflexion: Con esta actividad me quedo mas claro las capacidades que tiene el lenguaje de python.
# Dado que solo utilizé python anteriormente como calculadora y durante esta semana vimos cosas 
# gráficas vi que se pueden hacer progrmas que funcionen completamente por clicks. Y me hace pregunarme
# si se pueden hacer cosas al estilo paginas web desde cualquier legnuaje o si todos tienen capacidad
# de hacer videojuegos como python. 

from random import *
from turtle import *
from freegames import path

# Imagen de carro
car = path('car.gif')

# Diccionario global sobre el juego
state = {'mark': None, 'taps': 0}

# Lista de opciones
countries = ['Mexico','Russia','Inglaterra','Irlanda','Canada','Egipto','Grecia','Japon','China','Francia', 'India', 'Peru', 'Brasil' , 'Suecia','Argentina','Italia','Australia','Colombia','España','Noruega','Alemania','Panama','Vaticano','Suiza','USA','Holanda','UK','Iran','Sudafrica','Madagascar','Korea','Rapa Nui']
traditions = ['Taco','Vodka','Te','Trebol','Maple','Piramides','Zeus','Anime','Muralla','Eiffel','Taj Mahal', 'Machu Pichu','El Cristo', 'IKEA','Tango','Pasta','Arañas','Cafe','Paella','Vikingos','Oktoberfest','Canal','El Papa','Alpes','Hollywood','Tulipanes','Rugby','Persas','Zulu','Lemures','Kpop','Cabezas Piedra']

tiles = countries + traditions
for index in range(len(countries)):
    state[countries[index]] = index
    state[traditions[index]] = index

# Lista para saber si el tile puede ser revelado
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 215) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 215

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    
    # Variables necesarias para la logica
    spot = index(x, y)
    mark = state['mark']
    
    # Contador de taps
    state['taps'] += 1
    
    # Si ya se marco un lugar y este tap marca otro lugar que corresponde con el tile original, lo revela
    if mark is None or mark == spot or state[tiles[mark]] != state[tiles[spot]]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, -15)
    shape(car)
    stamp()
    
    # Contador de las parejas faltantes
    remaining = 0
    
    # Crear los cuadrados necesarios
    for count in range(64):
        if hide[count]:
            remaining += 1
            x, y = xy(count)
            square(x, y)
            
    # Desplegar resultados finales
    if(remaining == 0):
        up()
        goto(0,40)
        color('green')
        write("Well done\n You win!!", align = 'center', font = ('Arial',50,'bold'))
        goto(0,-180)
        write('Total taps:\n', align = 'center', font = ('Arial',30,'bold'))
        color('black')
        goto(0,-180)
        write(state['taps'], align = 'center', font = ('Arial',30,'bold'))
        color('black')
        goto(-200,185)
        write('Roberto Rodriguez   Luis Balderrama', align = 'left', font = ('Arial',17,'normal'))
        return

    # Mostrar el tile elegido por el momento
    mark = state['mark']
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 4, y+10)
        color('black')
        write(tiles[mark], font=('Arial', 8, 'normal'))
        
    # Desplegar el numero de taps hasta el momento
    up()
    goto(150,185)
    taps = state['taps']
    write(f'Taps: {taps}', align = 'center', font = ('Arial',20,'normal'))

    # Desplegar el numero de parejas que faltan
    goto(-110,185)
    remaining = int(remaining / 2)
    write(f'Remaining: {remaining}', align = 'center', font = ('Arial',20,'normal'))

    # Continuar con el juego
    update()
    ontimer(draw, 100)

# Barajear las cartas
shuffle(tiles)

# Crear la ventana
setup(420, 450, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
