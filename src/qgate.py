import numpy as np
from numpy.typing import NDArray

from .qbit import Qbit
from .util.qbitparser import qbitsToVector


class QGate:
    def __init__(self, matrix: NDArray):
        self.matrix = matrix

    def apply(self, state: list[Qbit], qbits_to_apply: list[int] = None):
        for qbit in state:
            vector = qbitsToVector([qbit])
            vector = np.dot(self.matrix, vector)
            qbit.a = vector[0]
            qbit.b = vector[1]

        return state

    def __str__(self):
        return str(self.matrix)

    def __repr__(self):
        return self.__str__()