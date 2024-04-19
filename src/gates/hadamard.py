import numpy as np

from ..qbit import Qbit
from ..qgate import QGate
from ..util.qbitparser import qbitsToVector, vectorToQbits


class Hadamard(QGate): 
    def __init__(self):
        super().__init__(None)
        
    def apply(self, state: list[Qbit], qbits_to_apply: list[int] = None):
        n_qbits = len(state)
        
        
        self._calculate_matrix(n_qbits)
        statevector = qbitsToVector(state)
        statevector = np.dot(self.matrix, statevector)
 
        return vectorToQbits(statevector)
    
    def _calculate_matrix(self, n_qbits: int):
        H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)  
        
        matrix = H
        
        for _ in range(n_qbits - 1):
            matrix = np.kron(matrix, H)
    
        self.matrix = matrix

    def __str__(self):
        return "Hadamard"