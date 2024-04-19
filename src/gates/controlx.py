import numpy as np

from ..qbit import Qbit
from ..qgate import QGate
from ..util.qbitparser import qbitsToVector, vectorToQbits


class ControlX(QGate): 
    def __init__(self):
        super().__init__(None)
        
    def apply(self, state: list[Qbit]):
        n_qbits = len(state)
        self._calculate_matrix(n_qbits)
        statevector = qbitsToVector(state)
        statevector = np.dot(self.matrix, statevector)

        return vectorToQbits(statevector)
    
    def _calculate_matrix(self, n_qbits: int):
        matrix = np.identity(2**n_qbits)
        matrix[-1, -1], matrix[-2, -2] = 0, 0
        matrix[-1, -2], matrix[-2, -1] = 1, 1

        self.matrix = matrix

    def __str__(self):
        return "Control-X"
