from typing import List, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np

from .gates.hadamard import Hadamard
from .gates.paulix import PauliX
from .gates.pauliy import PauliY
from .gates.pauliz import PauliZ
from .qgate import QGate
from .util.binaryparser import intToBinary


class QCircuit:
    def __init__(self, n_qubits: int, name: str="QCircuit"):
        self.n_qubits = n_qubits
        self.state = np.zeros(2**n_qubits, dtype=complex)
        self.state[0] = 1
        self.name = name
        self.gates: List[Tuple[QGate, int]] = []

    def h(self, qbits: Union[int, List[int], range]):
        self.append(Hadamard(), qbits)
        
    def x(self, qbits: Union[int, List[int], range]):
        self.append(PauliX(), qbits)
        
    def z(self, qbits: Union[int, List[int], range]):
        self.append(PauliZ(), qbits)
        
    def y(self, qbits: Union[int, List[int], range]):
        self.append(PauliY(), qbits)
        
    def append(self, gate: QGate, qubits: Union[int, List[int], range]):
        if isinstance(qubits, int):
            qubits = [qubits]
        elif isinstance(qubits, range):
            qubits = list(qubits)
            
        self.gates.append([gate, qubits])
        
    def run(self):
        for gate, qubits in self.gates:
            self.apply_gate(gate, qubits)
                
    def apply_gate(self, gate: QGate, qubits: List[int]):            
        qubit_indices = [1 if i in qubits else 0 for i in range(self.n_qubits)]
            
        self.state = gate.apply(self.state, qubit_indices)  
    
    def draw(self):
        vector = self.state
        states = [intToBinary(i, self.n_qubits) for i in range(len(vector))]
        colors = ['red' if amplitude < 0 else 'blue' for amplitude in vector]
        
        plt.bar(states, np.abs(vector), color=colors)
        plt.xlabel("State")
        plt.ylabel("Amplitude")
        plt.title(self.name)
        plt.xticks(rotation=90)
        plt.ylim(0, 1) 

        plt.show()

    def __str__(self):
        vector = self.state
        
        state_strings = ["==================================", "State:"]

        for i, amplitude in enumerate(vector):
            binary = intToBinary(i, int(np.log2(len(vector))))
            
            state_strings.append(f"{amplitude:.5f} |{binary}>")
        state_strings.append("==================================")  

        return "\n".join(state_strings)
    
    def __repr__(self):
        return self.__str__()