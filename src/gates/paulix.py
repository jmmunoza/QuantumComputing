import numpy as np

from ..qgate import QGate


class PauliX(QGate):
    def __init__(self):
        super().__init__(np.array([[0, 1], [1, 0]]))
        
    def __str__(self):
        return "X"