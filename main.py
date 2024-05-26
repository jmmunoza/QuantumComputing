from src.algorithms.grover.grover import Grover
from src.algorithms.grover.oracle import Oracle

"""
    Para ejecutar el programa, se debe correr el archivo main.py
    que se encuentra en la raíz del proyecto.
    
    Pero, antes que todo es necesario instalar las dependencias del proyecto,
    las cuales se encuentran en el archivo requirements.txt
    
    Numpy fue usado para el manejo de matrices y vectores, y Matplotlib para
    la visualización de los resultados.
"""
if __name__ == '__main__':
    # La función oráculo se encuentra fijada en 20, se creará un 
    # circuito de Grover con 6 qubits
    grover = Grover(Oracle(20), 6)
    
    # Se ejecuta el algoritmo
    grover.run()
    
    # Se dibuja el circuito
    grover.draw_circuit()
    
    # Se dibuja el estado final y se muestran sus AMPLITUDES (no probabilidades)
    grover.draw()
