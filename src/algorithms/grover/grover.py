import numpy as np

from ...gates.gdiffuser import GDiffuser
from ...qcircuit import QCircuit
from ...qgate import QGate


class Grover(QCircuit):
    def __init__(self, oracle: QGate, n_qubits: int):
        super().__init__(n_qubits, "Grover")
        
        n_iterations = int(np.pi / 4 * np.sqrt(2**n_qubits))-1
        
        print(n_iterations)
        
        self.h(range(n_qubits))
        
        for _ in range(n_iterations):
            # Apply the oracle
            self.apply_gate(oracle, range(n_qubits))
            self.h(range(n_qubits))

            self.apply_gate(GDiffuser(), range(n_qubits))
            self.h(range(n_qubits))

        
