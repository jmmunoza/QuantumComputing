from src.algorithms.grover.grover import Grover
from src.algorithms.grover.oracle import Oracle

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
