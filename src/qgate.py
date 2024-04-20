import numpy as np
from numpy.typing import NDArray


class QGate:
    def __init__(self, matrix: NDArray):
        self.matrix = matrix

    def apply(self, state: NDArray, qbits_to_apply: list[int] = None):
        n_qubits = len(qbits_to_apply)
        
        target_matrix = self.matrix if qbits_to_apply[-1] == 1 else np.eye(2)
        
        for i in range(1, n_qubits):
            target_matrix = np.kron(target_matrix, self.matrix if qbits_to_apply[n_qubits - 1 - i] == 1 else np.eye(2))
         
        return np.dot(target_matrix, state)

    def __str__(self):
        return str(self.matrix)

    def __repr__(self):
        return self.__str__()