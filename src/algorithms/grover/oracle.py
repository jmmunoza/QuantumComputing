import numpy as np
from numpy.typing import NDArray

from ...qgate import QGate


class Oracle(QGate):
    def __init__(self, value: int):
        super().__init__(None)
        self.value = value 
        
    def apply(self, state: NDArray, qbits_to_apply: list[int] = None):
        self.matrix = np.identity(2**len(qbits_to_apply))
        
        for i in range(2**len(qbits_to_apply)):
            if i == self.value:
                self.matrix[i, i] = -1

        return np.dot(self.matrix, state)
    
    def __str__(self):
        return f"Oracle ({self.value})"