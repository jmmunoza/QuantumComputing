import numpy as np

from ...qcircuit import QCircuit
from ...qgate import QGate
from .gdiffuser import GDiffuser


class Grover(QCircuit):
    def __init__(self, oracle: QGate, n_qubits: int):
        super().__init__(n_qubits, "Grover")
        
        n_iterations = int(np.pi / 4 * np.sqrt(2**n_qubits))-1

        self.h(range(n_qubits))
        
        for _ in range(n_iterations):
            self.append(oracle, range(n_qubits))
            self.h(range(n_qubits))

            self.append(GDiffuser(), range(n_qubits))
            self.h(range(n_qubits))

        
