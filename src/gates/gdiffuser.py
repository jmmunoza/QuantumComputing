import numpy as np
from numpy.typing import NDArray

from ..qgate import QGate


class GDiffuser(QGate): 
    def __init__(self):
        super().__init__(None)
        
    def apply(self, state: NDArray, qbits_to_apply: list[int] = None):
        self._calculate_matrix(len(qbits_to_apply))

        return np.dot(self.matrix, state)

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
