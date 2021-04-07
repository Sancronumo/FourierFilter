"""
Tarea 05 - Fourier - Filtrar señal (3) y Seal recuperada por transformada rápida inversa (4)

@autora: María Elena Esquivel Murillo
"""
'''
Ejercicio #1
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.fft

numeroPuntos=600
espaciado=1/800

frecuencia1=10
frecuencia2=20
amplitud1=15
amplitud2=30


valoresTiempo=np.linspace(0,numeroPuntos*espaciado,numeroPuntos,endpoint=False)


senal1=amplitud1*np.sin(2*np.pi*frecuencia1*valoresTiempo)
senal2=amplitud2*np.sin(2*np.pi*frecuencia2*valoresTiempo)
senal_pura=senal1+senal2

ruido=10/100*np.random.randint(-100,100,len(senal1))

senal_ruidosa=senal_pura+ruido

fig1, ax = plt.subplots()

ax.plot(valoresTiempo,senal_ruidosa,label='Señal Ruidosa')
ax.set_xlabel('Tiempo(s)')
ax.set_ylabel('Amplitud de la señal')
ax.set_title('Gráfica 1. Generación de Señal Ruidosa')

'''
Ejercicio #2
'''

fourierTransform=scipy.fft.fft(senal_ruidosa)
Frecuencias=scipy.fft.fftfreq(numeroPuntos,espaciado)[:int(numeroPuntos/2)]

fig2, ax= plt.subplots()


ax.plot(Frecuencias,2/numeroPuntos*np.abs(fourierTransform)[:int(numeroPuntos/2)],label='Señal Pura')
ax.set_xlabel('Frecuencias(Hz)')
ax.set_ylabel('Intensidad')
ax.set_title('Gráfica 2. Gráfico de la tranformada de fourier en el dominio de la frecuencia')

'''
Ejercicio #3
'''

def Filtrar_Señal (señal, umbral):
    for k in range(0, len(señal)):
        if np.abs(señal[k])<umbral:
            señal[k]=0
    return señal

fourierTransformFiltrada=Filtrar_Señal (2/numeroPuntos*fourierTransform, 5)

fig3, ax= plt.subplots()

ax.plot(Frecuencias,np.abs(fourierTransformFiltrada)[:int(numeroPuntos/2)],label='Señal Filtrada')
ax.set_xlabel('Frecuencias(Hz)')
ax.set_ylabel('Intensidad')
ax.set_title('Gráfica 3. Gráfico de la tranformada de fourier filtrada en el dominio de la frecuencia')

'''
Ejercicio #4
'''

señalFiltrada=scipy.fft.ifft(fourierTransformFiltrada*numeroPuntos/2)

fig4, ax = plt.subplots()

ax.plot(valoresTiempo,señalFiltrada,label='Señal Filtrada')
ax.set_xlabel('Tiempo(s)')
ax.set_ylabel('Amplitud de la señal')
ax.set_title('Gráfica 4. Señal recuperada')