import numpy as np

from ..qbit import Qbit
from ..qgate import QGate
from ..util.qbitparser import qbitsToVector, vectorToQbits


class GDiffuser(QGate): 
    def __init__(self):
        super().__init__(None)
        
    def apply(self, state: list[Qbit]):
        n_qbits = len(state)
        self._calculate_matrix(n_qbits)
        statevector = qbitsToVector(state)
        statevector = np.dot(self.matrix, statevector)
      
        return vectorToQbits(statevector)
    '''
    Generates the matrix for the Grover diffuser
        
    [[1 0 0 0 ... 0]
     [0 -1 0 0 ... 0]
     [0 0 -1 0 ... 0]
     ...
     [0 0 0 0 ... -1]]
    '''
    def _calculate_matrix(self, n_qbits: int):
        self.matrix = np.identity(2**n_qbits)
        
        for i in range(1, 2**n_qbits):
            self.matrix[i, i] = -1

    def __str__(self):
        return "Hadamard"
