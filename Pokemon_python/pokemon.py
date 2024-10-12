import numpy as np

import sys

import time

                                                    # Función para imprimir con retraso
def imprimir_con_retraso(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

                                                       # Clase Pokémon
class Pokemon:
    def __init__(self, nombre, tipos, movimientos, EVs, puntos_de_salud='===================='):
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.ataque = EVs['Ataque']
        self.defensa = EVs['defensa']
        self.puntos_de_salud = puntos_de_salud
        self.barras = 20                          # Cantidad de barras de puntos de salud

    def impresa(self, pokemon2):
        '''Imprimir información de lucha'''
        print("----BATALLA POKEMON----")
        print(f"\n{self.nombre}")
        print("Tipo:", self.tipos)
        print("Ataque:", self.ataque)
        print("Defensa:", self.defensa)
        print("Nv.:", 3 * (1 + np.mean([self.ataque, self.defensa])))
        print("\nVS")
        print(f"{pokemon2.nombre}")
        print("Tipo:", pokemon2.tipos)
        print("Ataque:", pokemon2.ataque)
        print("Defensa:", pokemon2.defensa)
        print("Nv.:", 3 * (1 + np.mean([pokemon2.ataque, pokemon2.defensa])))

    def ventajas(self, pokemon2):
        '''Considera la ventaja de tipo y devuelve el resultado de la pelea'''
        tipos = ['fuego', 'agua', 'planta']
        cadena_1_ataque = ''
        cadena_2_ataque = ''
        for i, k in enumerate(tipos):
            if self.tipos == k:
                if pokemon2.tipos == k:
                    cadena_1_ataque = '\nNo es muy efectivo...'
                    cadena_2_ataque = '\nNo es muy efectivo...'
                elif pokemon2.tipos == tipos[(i + 1) % 3]:
                    pokemon2.ataque *= 2
                    pokemon2.defensa *= 2
                    self.ataque /= 2
                    self.defensa /= 2
                    cadena_1_ataque = '\nNo es muy efectivo...'
                    cadena_2_ataque = '\n¡Es muy eficaz!'
                elif pokemon2.tipos == tipos[(i + 2) % 3]:
                    self.ataque *= 2
                    self.defensa *= 2
                    pokemon2.ataque /= 2
                    pokemon2.defensa /= 2
                    cadena_1_ataque = '\n¡Es muy eficaz!'
                    cadena_2_ataque = '\nNo es muy efectivo...'
        return cadena_1_ataque, cadena_2_ataque

    def turno(self, pokemon2, cadena_1_ataque, cadena_2_ataque):
        '''Simula el turno de combate entre ambos Pokémon'''
        while self.barras > 0 and pokemon2.barras > 0:
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"\n{pokemon2.nombre}\t\tPS\t{pokemon2.puntos_de_salud}\n")

                                                          # Turno del primer Pokémon
            print(f"¡Adelante {self.nombre}!")
            for i, x in enumerate(self.movimientos):
                print(f"{i+1}.", x)
            index = int(input('Elige un movimiento: '))
            imprimir_con_retraso(f"\n¡{self.nombre} usó {self.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_1_ataque)

            pokemon2.barras -= self.ataque
            pokemon2.puntos_de_salud = ""                # Reinicializar los puntos de salud
            for j in range(int(pokemon2.barras + .1 * pokemon2.defensa)):
                pokemon2.puntos_de_salud += "="
            time.sleep(1)

            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"{pokemon2.nombre}\t\tPS\t{pokemon2.puntos_de_salud}\n")
            time.sleep(.5)

            if pokemon2.barras <= 0:
                imprimir_con_retraso("\n..." + pokemon2.nombre + ' se debilitó')
                break

                                                        # Turno del segundo Pokémon
            print(f"¡Adelante {pokemon2.nombre}!")
            for i, x in enumerate(pokemon2.movimientos):
                print(f"{i+1}.", x)
            index = int(input('Elige un movimiento: '))
            imprimir_con_retraso(f"\n¡{pokemon2.nombre} usó {pokemon2.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_2_ataque)

            self.barras -= pokemon2.ataque
            self.puntos_de_salud = "" 
            
                                                        # Reinicializar los puntos de salud

            for j in range(int(self.barras + .1 * self.defensa)):
                self.puntos_de_salud += "="
            time.sleep(1)

            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"{pokemon2.nombre}\t\tPS\t{pokemon2.puntos_de_salud}\n")
            time.sleep(.5)

            if self.barras <= 0:
                imprimir_con_retraso("\n..." + self.nombre + ' se debilitó')
                break

    def lucha(self, pokemon2):
        '''Permitir que los Pokémon luchen entre ellos'''
        self.impresa(pokemon2)
        cadena_1_ataque, cadena_2_ataque = self.ventajas(pokemon2)
        self.turno(pokemon2, cadena_1_ataque, cadena_2_ataque)

                                                           # Recibir premio
money = np.random.choice(5000)
imprimir_con_retraso(f"\nEl oponente te pagó ${money}\n")

                                                         # Crear Pokémon objetos
if __name__ == '__main__':
 charizard = Pokemon('Charizard', 'fuego', ['lanzallamas', 'pirotecnia', 'giro de fuego', 'ascuas'], {'Ataque': 12, 'defensa': 8})
 blastoise = Pokemon('Blastoise', 'agua', ['hidrobomba', 'pistola agua', 'cascada', 'surf'], {'Ataque': 10, 'defensa': 12})
 venusaur = Pokemon('Venusaur', 'planta', ['latigazo', 'hoja afilada', 'síntesis', 'rayo solar'], {'Ataque': 11, 'defensa': 10})
 pikachu = Pokemon('Pikachu', 'eléctrico', ['impactrueno', 'rayo', 'trueno', 'ataque rápido'], {'Ataque': 8, 'defensa': 6})
 alakazam = Pokemon('Alakazam', 'psíquico', ['psíquico', 'confusión', 'telequinesis', 'deslumbrar'], {'Ataque': 13, 'defensa': 7})
 machamp = Pokemon('Machamp', 'lucha', ['golpe karate', 'puño dinámico', 'demolición', 'puño fuego'], {'Ataque': 14, 'defensa': 9})
 gengar = Pokemon('Gengar', 'fantasma', ['bola sombra', 'lengüetazo', 'terror nocturno', 'puño sombra'], {'Ataque': 12, 'defensa': 8})
 snorlax = Pokemon('Snorlax', 'normal', ['golpe cuerpo', 'descanso', 'bostezo', 'terremoto'], {'Ataque': 11, 'defensa': 14})
 dragonite = Pokemon('Dragonite', 'dragón', ['vuelo', 'enfado', 'hiper rayo', 'cometa draco'], {'Ataque': 15, 'defensa': 10})
 jolteon = Pokemon('Jolteon', 'eléctrico', ['impactrueno', 'voltio cruel', 'rayo', 'chispazo'], {'Ataque': 11, 'defensa': 8})
 lapras = Pokemon('Lapras', 'agua/hielo', ['hidrobomba', 'rayo hielo', 'surf', 'canto'], {'Ataque': 10, 'defensa': 12})
 arcanine = Pokemon('Arcanine', 'fuego', ['lanzallamas', 'colmillo ígneo', 'rueda fuego', 'giro fuego'], {'Ataque': 12, 'defensa': 9})
 gyarados = Pokemon('Gyarados', 'agua/volador', ['hidrobomba', 'pulso dragón', 'salpicadura', 'rayo hielo'], {'Ataque': 14, 'defensa': 10})
 exeggutor = Pokemon('Exeggutor', 'planta/psíquico', ['rayo solar', 'psíquico', 'hoja afilada', 'explosión'], {'Ataque': 11, 'defensa': 9})
 electabuzz = Pokemon('Electabuzz', 'eléctrico', ['rayo', 'trueno', 'ataque rápido', 'pantalla de luz'], {'Ataque': 12, 'defensa': 7})
 rhydon = Pokemon('Rhydon', 'roca/tierra', ['terremoto', 'avalancha', 'roca afilada', 'golpe roca'], {'Ataque': 14, 'defensa': 11})
 scyther = Pokemon('Scyther', 'bicho/volador', ['corte', 'danza espada', 'golpe aéreo', 'ataque rápido'], {'Ataque': 13, 'defensa': 8})
 magmar = Pokemon('Magmar', 'fuego', ['lanzallamas', 'puño fuego', 'giro fuego', 'ascuas'], {'Ataque': 11, 'defensa': 7})
 flareon = Pokemon('Flareon', 'fuego', ['lanzallamas', 'pirotecnia', 'giro fuego', 'ascuas'], {'Ataque': 12, 'defensa': 8})
 charizard.lucha(gyarados)

