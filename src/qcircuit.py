from typing import List, Union

import matplotlib.pyplot as plt

from .gates.controlx import ControlX
from .gates.hadamard import Hadamard
from .gates.paulix import PauliX
from .gates.pauliy import PauliY
from .gates.pauliz import PauliZ
from .qbit import Qbit
from .qgate import QGate
from .util.binaryparser import intToBinary
from .util.qbitparser import qbitsToVector


class QCircuit:
    def __init__(self, n_qbits: int, name: str="QCircuit"):
        self.qbits = [Qbit(1, 0) for _ in range(n_qbits)]
        self.gates: list[list[QGate]] = []
        self.name = name

    def h(self, qbits: Union[int, List[int], range]):
        self.apply_gate(Hadamard(), qbits)
        
    def x(self, qbits: Union[int, List[int], range]):
        self.apply_gate(PauliX(), qbits)
        
    def z(self, qbits: Union[int, List[int], range]):
        self.apply_gate(PauliZ(), qbits)
        
    def y(self, qbits: Union[int, List[int], range]):
        self.apply_gate(PauliY(), qbits)
        
    def cx(self, qbits: Union[int, List[int], range]):
        self.apply_gate(ControlX(), qbits)
                
    def apply_gate(self, gate: QGate, qbits: Union[int, List[int], range]):
        if isinstance(qbits, int):
            qbits_to_apply = [qbits]
        elif isinstance(qbits, range):
            qbits_to_apply = list(qbits)
        else: 
            qbits_to_apply = qbits
            
        self.qbits = gate.apply(self.qbits, qbits_to_apply)  
            
        for i, qbit in enumerate(self.qbits):
            print(f"Qbit {i}: {qbit}")
    
    def draw(self):
        vector = qbitsToVector(self.qbits)
 
        states = [intToBinary(i, len(self.qbits)) for i in range(2**len(self.qbits))]

        plt.bar(states, vector)
        plt.xlabel("State")
        plt.ylabel("Amplitude")
        plt.title(self.name)
        plt.xticks(rotation=90)
        plt.ylim(-1, 1) 

        plt.show()
                
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        vector = qbitsToVector(self.qbits)
        
        state_strings = ["==================================", "State:"]

        for i, amplitude in enumerate(vector):
            state_strings.append(f"{amplitude:.10f} |{intToBinary(i, len(self.qbits))}>")

        state_strings.append("==================================")  

        return "\n".join(state_strings)