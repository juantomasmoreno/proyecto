# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 08:35:48 2022

@author: adrir
"""

import csv
import os
import matplotlib.pyplot as plt


class Jugador:
    def __init__(self,ide, nombre,posicion,media,potencial,edad,altura,club,liga,nivelLiga,pais,pDom,fifa,nCorto):
        self.ide = ide
        self.nombre = nombre
        self.posicion = [posicion]
        self.media=[media]
        self.potencial =[potencial]
        self.edad = [edad]
        self.altura = altura
        self.club=[club]
        self.liga=liga
        self.nivelLiga=nivelLiga
        self.pais= pais
        self.pDom=pDom
        self.fifa= [fifa]
        self.nCorto=nCorto
        

    

class Clase:
    def __init__(self):
        self.jugadores = {}
        
    def nuevo_jugador(self,ide,nombre ,posicion,media,potencial,edad,altura,club,liga,nivelLiga,pais,pDom,fifa,nCorto):
        if ide in self.jugadores.keys():
            jugador=self.jugadores[ide]
            jugador.fifa.append(fifa)
            jugador.posicion.append(posicion)
            jugador.media.append(media)
            jugador.potencial.append(potencial)
            jugador.club.append(club)
            jugador.edad.append(edad)
            return False, ''
            
        else:
            self.jugadores[ide] = Jugador(ide,nombre ,posicion,media,potencial,edad,altura,club,liga,nivelLiga,pais,pDom,fifa,nCorto)
            return True, 'Añadido correctamente'
    
    def cargar_datos(self, fichero):
        try:
            with open(fichero,'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                leidos = 0
                next(reader)
                for sofifa_id,long_name,player_positions,overall,potential,age,height_cm,club_name,league_name,league_level,nationality_name,preferred_foot,FIFA,short_name in reader:
                    b, msg = self.nuevo_jugador(sofifa_id,long_name,player_positions,int(overall),potential,age,height_cm,club_name,league_name,league_level,nationality_name,preferred_foot,FIFA,short_name)
                    
                    if b:                 
                        leidos += 1
                    
                print ( f'{leidos} jugadores leidos correctamente')
                return True, 'correcto'
        except Exception as ex:
            print ( 'Error al leer fichero de datos. Excepcion de tipo '+
                    f'{type(ex).__name__}\nArgumentos:{ex.args}. \n'+
                    f'Directorio actual:{os.getcwd()}')


        
    def buscar(self):
        texto = ''
        n = 1
        dic = {}
        while len(texto) < 3 or not dic:
            texto = input('¿A quién buscas?: ').lower()
            if len(texto) < 3:
                print('Introduce más carácteres en la búsqueda')
            else:
                for ide,jugador in self.jugadores.items():
                    if texto in jugador.nombre.lower().split(): 
                        print(f'{n} {jugador.nombre}')
                        dic[n] = ide
                        n += 1
                    elif texto in jugador.nCorto.lower().split():
                        print(f'{n} {jugador.nCorto}')
                        dic[n] = ide
                        n += 1
                if not dic:
                    print('No hay ningún jugador con esa búsqueda')
                    texto = ''
        elec = 0
        while elec < 1 or elec > len(dic):
            try:
                elec = int(input('Elige un jugador: '))
            except:
                elec = 0
        return dic[elec]
        
    def grafica_media(self,jugador):
        x=self.jugadores[jugador]
        plt.grid(axis='x')
        plt.grid(axis='y')
        plt.title(f'Evolución de {x.nCorto}')
        plt.plot(x.fifa,x.media)
c=Clase()
c.cargar_datos('Career_Mode_FIFA.csv')
jugador=c.buscar() 
c.grafica_media(jugador)


