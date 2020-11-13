#!/usr/bin/python3
'''
SIMULACION DE UN SISTEMA DE COMUNICACIONES CON CODIFICADOR
DE CANAL, CANAL BINARIO SIMETRICO + MODULACION + 
DEMODULACION + DECODIFICADOR DE CANALCON CORRECCION DE ERRORES
'''

#Paquetes
import numpy as np
from PIL import Image
from src.modulation import *
from src.channel import *
from src.source import *

#=============CON MEDIO IDEAL==============
'''
1. Se inicializa la fuente de informacion
y se llama al codificador de fuente
'''
fuente_info = image_source('/home/jussc_/Desktop/Comunicaciones/Proyecto_simulado/src/dar.bmp')
x, y, z = fuente_info.shape
vT, bfT, r = source_encoder(fuente_info)
'''
2. Parametros dimensionales: m es el numero
de paquetes 1xk obtenidos del codificador
de fuente en bits; n > k
'''
m, k = bfT.shape
n = 16
'''
3. Se inicializa el objeto sistema, que cuenta
con codificador de canal, canal simetrico
'''
#Se crea el objeto sistema:
sistema = com_sys(m, k, n) 
bcT = sistema.channel_encoder(bfT)
'''
4. Se inicializa el modulador, medio
ideal y desmodulador
'''
modem = modulation(m, k, n)
an = modem.symbol_modulator(bcT)
pam = modem.PAM(an)
yn = modem.symbol_demodulator(an)
'''
5. Se inicializa decodificador de canal.
'''
bfR = sistema.channel_decoder(yn)
'''
6. Se llama al decodificador de fuente
y se simula el sumidero para recuperar
la imagen transmitida.
'''
vR = source_Decoder(bfR, x, y, True, 8)
sumidero = Image.fromarray(vR)
sumidero.show()