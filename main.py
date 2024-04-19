from typing import List, Union

import numpy as np

from src.qcircuit import QCircuit

#if __name__ == '__main__':
#    circuit = QCircuit(2)
#    circuit.h(0)

    #circuit.draw()






class Qubit:
    def __init__(self, a: complex, b: complex):
        self.a = a
        self.b = b

class QuantumSimulator:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = np.zeros(2**num_qubits, dtype=complex)
        self.state[0] = 1  # Initialize to |0> state

    def apply_hadamard_gate(self, target_qubits: Union[int, List[int], range]):
        hadamard_matrix = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
        
        if isinstance(target_qubits, int):
            target_qubits = [target_qubits]
        elif isinstance(target_qubits, range):
            target_qubits = list(target_qubits)
        
        qubit_indices = [1 if i in target_qubits else 0 for i in range(self.num_qubits)]
        
        if len(target_qubits) == 0:
            pass
        
        target_matrix = hadamard_matrix if qubit_indices[-1] == 1 else np.eye(2)
        
        for i in range(1, self.num_qubits):
            target_matrix = np.kron(target_matrix, hadamard_matrix if qubit_indices[self.num_qubits - 1 - i] == 1 else np.eye(2))
        
            
        self.state = np.dot(target_matrix, self.state)


# Ejemplo de uso
simulator = QuantumSimulator(num_qubits=4)

simulator.apply_hadamard_gate(target_qubits=range(4))
simulator.apply_hadamard_gate(target_qubits=[0, 1])
print( simulator.state)